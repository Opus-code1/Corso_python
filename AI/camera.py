"""Controlla il puntatore del mouse seguendo la punta dell'indice.

Versione 2:
- cattura webcam in un thread dedicato (sempre l'ultimo frame, zero coda);
- pyautogui senza pause artificiali (PAUSE = 0);
- filtro One Euro adattivo (fermo = stabile, veloce = reattivo);
- anti-drift al click (il cursore non scivola quando chiudi il pinch);
- pose stabilizzate su piu' frame (niente scatti da riconoscimenti isolati);
- precisione sub-pixel (accumulo in float);
- distanze calcolate in pixel (niente distorsione 4:3);
- tolleranza ai buchi di tracking (un trascinamento non si rompe per 1-2 frame persi).

Tasti nella finestra: Q/ESC esci, P pausa. Uscita di emergenza: porta il mouse
FISICO nell'angolo in alto a sinistra (la mano non puo' raggiungerlo).
"""

from __future__ import annotations

import math
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


URL_MODELLO = (
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/1/hand_landmarker.task"
)

# Indici dei landmark MediaPipe
POLSO = 0
POLLICE_PUNTA = 4
INDICE_MCP = 5
INDICE_PIP = 6
INDICE_PUNTA = 8
MEDIO_MCP = 9
MEDIO_PIP = 10
MEDIO_PUNTA = 12
ANULARE_PIP = 14
ANULARE_PUNTA = 16
MIGNOLO_MCP = 17
MIGNOLO_PIP = 18
MIGNOLO_PUNTA = 20


@dataclass(frozen=True)
class Config:
    # Webcam
    camera_indice: int = 0
    larghezza_cam: int = 640
    altezza_cam: int = 480
    fps_cam: int = 30

    # Area attiva della webcam mappata sullo schermo (0.12 = 12% di margine per lato).
    # Piu' piccola = meno movimento del braccio, ma piu' amplificazione del tremore.
    margine_x: float = 0.12
    margine_y: float = 0.12

    # Filtro One Euro (coordinate normalizzate 0..1)
    # mincutoff: piu' basso = piu' stabile da fermo (ma piu' lento a partire)
    # beta:      piu' alto  = meno lag quando ti muovi veloce (ma piu' jitter)
    filtro_mincutoff: float = 1.4
    filtro_beta: float = 14.0
    filtro_dcutoff: float = 1.0

    # Precisione
    fattore_precisione: float = 0.3
    zona_morta_precisione: float = 0.0003
    hold_precisione: float = 0.65

    # Pinch (distanze normalizzate sulla scala della mano)
    soglia_pinch: float = 0.32
    rilascio_pinch: float = 0.48
    conferma_sinistro: float = 0.09
    conferma_destro: float = 0.20

    # Anti-drift: al pinch il cursore torna alla posizione di N secondi prima
    rollback_click_s: float = 0.10
    # Dopo il click, il cursore rientra sulla mano in questo tempo (costante)
    rientro_s: float = 0.25

    # Scroll
    passo_scroll: float = 0.035

    # Robustezza
    frame_stabilita_posa: int = 3
    tolleranza_perdita_s: float = 0.25


class PuntoMano(Protocol):
    x: float
    y: float


def _dist(a: PuntoMano, b: PuntoMano, w: int, h: int) -> float:
    """Distanza in pixel (le coordinate normalizzate x/y non hanno la stessa scala)."""
    return math.hypot((a.x - b.x) * w, (a.y - b.y) * h)


def _esteso(mano: Sequence[PuntoMano], punta: int, pip: int, w: int, h: int) -> bool:
    """Dito esteso = punta piu' lontana dal polso del PIP. Funziona anche con la mano ruotata."""
    polso = mano[POLSO]
    return _dist(mano[punta], polso, w, h) > _dist(mano[pip], polso, w, h) * 1.1


def _classifica_posa(mano: Sequence[PuntoMano], w: int, h: int) -> str:
    indice = _esteso(mano, INDICE_PUNTA, INDICE_PIP, w, h)
    medio = _esteso(mano, MEDIO_PUNTA, MEDIO_PIP, w, h)
    anulare = _esteso(mano, ANULARE_PUNTA, ANULARE_PIP, w, h)
    mignolo = _esteso(mano, MIGNOLO_PUNTA, MIGNOLO_PIP, w, h)
    if indice and medio and anulare and not mignolo:
        return "precisione"
    if indice and medio and not anulare and not mignolo:
        return "scorrimento"
    return "puntatore"


class StabilizzaPosa:
    """Cambia posa solo dopo N frame consecutivi uguali."""

    def __init__(self, frame: int) -> None:
        self.frame = max(1, frame)
        self.reset()

    def reset(self) -> None:
        self.corrente = "puntatore"
        self._candidata: str | None = None
        self._conteggio = 0

    def aggiorna(self, posa: str) -> str:
        if posa == self.corrente:
            self._candidata = None
            self._conteggio = 0
        elif posa == self._candidata:
            self._conteggio += 1
        else:
            self._candidata = posa
            self._conteggio = 1
        if self._candidata is not None and self._conteggio >= self.frame:
            self.corrente = self._candidata
            self._candidata = None
            self._conteggio = 0
        return self.corrente


class FiltroOneEuro:
    """One Euro Filter (Casiez et al.): taglio adattivo alla velocita'."""

    def __init__(self, mincutoff: float, beta: float, dcutoff: float) -> None:
        self.mincutoff = mincutoff
        self.beta = beta
        self.dcutoff = dcutoff
        self.reset()

    def reset(self) -> None:
        self._x: float | None = None
        self._dx = 0.0
        self._t: float | None = None

    @staticmethod
    def _alpha(cutoff: float, dt: float) -> float:
        tau = 1.0 / (2.0 * math.pi * cutoff)
        return 1.0 / (1.0 + tau / dt)

    def filtra(self, x: float, t: float) -> float:
        if self._x is None or self._t is None:
            self._x, self._t, self._dx = x, t, 0.0
            return x
        dt = max(t - self._t, 1e-3)
        dx = (x - self._x) / dt
        a_d = self._alpha(self.dcutoff, dt)
        self._dx = a_d * dx + (1.0 - a_d) * self._dx
        cutoff = self.mincutoff + self.beta * abs(self._dx)
        a = self._alpha(cutoff, dt)
        self._x = a * x + (1.0 - a) * self._x
        self._t = t
        return self._x


class Puntatore:
    """Converte la posizione dell'indice in posizione del cursore (float, sub-pixel)."""

    def __init__(self, cfg: Config, larghezza: int, altezza: int) -> None:
        self.cfg = cfg
        self.w = larghezza
        self.h = altezza
        self.fx = FiltroOneEuro(cfg.filtro_mincutoff, cfg.filtro_beta, cfg.filtro_dcutoff)
        self.fy = FiltroOneEuro(cfg.filtro_mincutoff, cfg.filtro_beta, cfg.filtro_dcutoff)
        self.storico: deque[tuple[float, float, float]] = deque(maxlen=60)
        self.cursore: tuple[float, float] | None = None
        self.offset = (0.0, 0.0)
        self._t_prec: float | None = None
        self._dito_prec: tuple[float, float] | None = None
        self._precisione_prec = False
        self._nuova_sessione = True

    def reset(self) -> None:
        self.fx.reset()
        self.fy.reset()
        self.storico.clear()
        self._t_prec = None
        self._dito_prec = None
        self._nuova_sessione = True

    def _assoluto(self, fx: float, fy: float) -> tuple[float, float]:
        c = self.cfg
        qx = min(max(fx, c.margine_x), 1 - c.margine_x)
        qy = min(max(fy, c.margine_y), 1 - c.margine_y)
        px = (qx - c.margine_x) / (1 - 2 * c.margine_x) * (self.w - 1)
        py = (qy - c.margine_y) / (1 - 2 * c.margine_y) * (self.h - 1)
        return px, py

    def _limita(self, x: float, y: float) -> tuple[float, float]:
        # Mai (0, 0): e' l'angolo del failsafe di pyautogui, riservato al mouse fisico.
        return min(max(x, 1.0), self.w - 2.0), min(max(y, 1.0), self.h - 2.0)

    def riavvolgi(self, t: float) -> None:
        """Al primo istante di pinch riporta il cursore dove era prima che le dita si muovessero."""
        if (
            self._precisione_prec
            or self.cursore is None
            or self.cfg.rollback_click_s <= 0
        ):
            return
        limite = t - self.cfg.rollback_click_s
        scelto = None
        for voce in self.storico:
            if voce[0] <= limite:
                scelto = voce
            else:
                break
        if scelto is None:
            return
        ax, ay = self._assoluto(scelto[1], scelto[2])
        self.cursore = self._limita(ax + self.offset[0], ay + self.offset[1])

    def aggiorna(
        self,
        x: float,
        y: float,
        t: float,
        precisione: bool,
        stato: str,
        reale: tuple[int, int],
    ) -> tuple[float, float]:
        """stato: 'libero' (segue la mano), 'fermo' (cursore bloccato), 'trascinamento'."""
        cfg = self.cfg
        fx = self.fx.filtra(x, t)
        fy = self.fy.filtra(y, t)
        self.storico.append((t, fx, fy))
        dt = 0.033 if self._t_prec is None else max(t - self._t_prec, 1e-3)
        self._t_prec = t
        ax, ay = self._assoluto(fx, fy)

        # Risincronizzazione: primo frame, mouse fisico spostato, ritorno dopo perdita mano.
        if (
            self.cursore is None
            or math.hypot(reale[0] - self.cursore[0], reale[1] - self.cursore[1]) > 4.0
        ):
            self.cursore = (float(reale[0]), float(reale[1]))
            self.offset = (self.cursore[0] - ax, self.cursore[1] - ay)
            self._dito_prec = None
            self._nuova_sessione = False
        elif self._nuova_sessione:
            self.offset = (self.cursore[0] - ax, self.cursore[1] - ay)
            self._dito_prec = None
            self._nuova_sessione = False

        if precisione != self._precisione_prec:
            if precisione:
                self._dito_prec = (fx, fy)
            else:
                self.offset = (self.cursore[0] - ax, self.cursore[1] - ay)
            self._precisione_prec = precisione

        if precisione:
            if stato != "fermo" and self._dito_prec is not None:
                dfx = fx - self._dito_prec[0]
                dfy = fy - self._dito_prec[1]
                if math.hypot(dfx, dfy) < cfg.zona_morta_precisione:
                    dfx = dfy = 0.0
                kx = self.w / (1 - 2 * cfg.margine_x) * cfg.fattore_precisione
                ky = self.h / (1 - 2 * cfg.margine_y) * cfg.fattore_precisione
                self.cursore = (self.cursore[0] + dfx * kx, self.cursore[1] + dfy * ky)
            self._dito_prec = (fx, fy)
        else:
            if stato == "fermo":
                self.offset = (self.cursore[0] - ax, self.cursore[1] - ay)
            elif stato == "libero":
                k = math.exp(-dt / cfg.rientro_s)
                ox, oy = self.offset[0] * k, self.offset[1] * k
                if abs(ox) < 0.5 and abs(oy) < 0.5:
                    ox = oy = 0.0
                self.offset = (ox, oy)
            self.cursore = (ax + self.offset[0], ay + self.offset[1])

        self.cursore = self._limita(*self.cursore)
        return self.cursore


class ControlloMouse:
    """Macchina a stati dei gesti -> azioni del mouse."""

    def __init__(self, cfg: Config, pag) -> None:  # noqa: ANN001
        self.cfg = cfg
        self.pag = pag
        larghezza, altezza = pag.size()
        self.puntatore = Puntatore(cfg, larghezza, altezza)
        self.posa = StabilizzaPosa(cfg.frame_stabilita_posa)
        self.precisione = False
        self.pausa = False
        self.ultimo_visto: float | None = None
        self._inizio_precisione: float | None = None
        self._precisione_bloccata = False
        self._y_scroll: float | None = None
        self._acc_scroll = 0.0
        self._d_idx: float | None = None
        self._d_med: float | None = None
        self._sx_attivo = False
        self._sx_inizio: float | None = None
        self._sx_premuto = False
        self._dx_attivo = False
        self._dx_inizio: float | None = None
        self._dx_eseguito = False
        self._ultimo_inviato: tuple[int, int] | None = None

    def rilascia_tutto(self) -> None:
        if self._sx_premuto:
            self.pag.mouseUp(button="left", _pause=False)
        self._sx_premuto = False
        self._sx_attivo = False
        self._sx_inizio = None
        self._dx_attivo = False
        self._dx_inizio = None
        self._dx_eseguito = False

    def alterna_pausa(self) -> None:
        self.pausa = not self.pausa
        self.rilascia_tutto()
        self.puntatore.reset()

    def mano_persa(self, t: float) -> None:
        if self.ultimo_visto is None:
            return
        if t - self.ultimo_visto < self.cfg.tolleranza_perdita_s:
            return  # buco breve: mantieni stato (il drag non si spezza)
        self.rilascia_tutto()
        self.puntatore.reset()
        self.posa.reset()
        self._inizio_precisione = None
        self._precisione_bloccata = False
        self._y_scroll = None
        self._acc_scroll = 0.0
        self._d_idx = self._d_med = None
        self.ultimo_visto = None

    def _muovi(self, x: float, y: float) -> None:
        xi, yi = int(round(x)), int(round(y))
        if (xi, yi) != self._ultimo_inviato:
            self.pag.moveTo(xi, yi, _pause=False)
            self._ultimo_inviato = (xi, yi)

    def elabora(self, mano: Sequence[PuntoMano], t: float, wv: int, hv: int) -> str:
        cfg = self.cfg
        pag = self.pag
        self.ultimo_visto = t
        posa = self.posa.aggiorna(_classifica_posa(mano, wv, hv))
        punta = mano[INDICE_PUNTA]
        testo = "Indice: muovi | Pinch pollice-indice: click/trascina"

        # --- Toggle precisione (tre dita tenute) ---
        if posa == "precisione":
            if self._inizio_precisione is None:
                self._inizio_precisione = t
            elif (
                not self._precisione_bloccata
                and t - self._inizio_precisione >= cfg.hold_precisione
            ):
                self.precisione = not self.precisione
                self._precisione_bloccata = True
            testo = "Tieni tre dita alzate per attivare/disattivare la precisione"
        else:
            self._inizio_precisione = None
            self._precisione_bloccata = False

        # --- Scroll (indice + medio) ---
        if posa == "scorrimento":
            if self._y_scroll is not None:
                delta = min(max(self._y_scroll - punta.y, -0.12), 0.12)
                self._acc_scroll += delta
                while abs(self._acc_scroll) >= cfg.passo_scroll:
                    direzione = 1 if self._acc_scroll > 0 else -1
                    pag.scroll(direzione, _pause=False)
                    self._acc_scroll -= direzione * cfg.passo_scroll
            self._y_scroll = punta.y
            testo = "Scorrimento: muovi indice e medio in alto o in basso"
        else:
            self._y_scroll = None
            self._acc_scroll = 0.0

        # --- Pinch (solo in posa puntatore) ---
        pinch_sx = pinch_dx = False
        if posa == "puntatore":
            scala = max(
                _dist(mano[POLSO], mano[MEDIO_MCP], wv, hv),
                _dist(mano[INDICE_MCP], mano[MIGNOLO_MCP], wv, hv),
                1.0,
            )
            d_i = _dist(mano[POLLICE_PUNTA], punta, wv, hv) / scala
            d_m = _dist(mano[POLLICE_PUNTA], mano[MEDIO_PUNTA], wv, hv) / scala
            self._d_idx = d_i if self._d_idx is None else 0.5 * self._d_idx + 0.5 * d_i
            self._d_med = d_m if self._d_med is None else 0.5 * self._d_med + 0.5 * d_m
            pinch_dx = (
                self._d_med < (cfg.rilascio_pinch if self._dx_attivo else cfg.soglia_pinch)
                and self._d_idx > cfg.rilascio_pinch
            )
            pinch_sx = not pinch_dx and self._d_idx < (
                cfg.rilascio_pinch if self._sx_attivo else cfg.soglia_pinch
            )
        else:
            self._d_idx = self._d_med = None

        # --- Movimento del cursore ---
        if posa == "puntatore":
            if (pinch_sx and not self._sx_attivo) or (pinch_dx and not self._dx_attivo):
                self.puntatore.riavvolgi(t)
            if self._sx_premuto and pinch_sx:
                stato = "trascinamento"
            elif pinch_sx or pinch_dx or self._sx_premuto:
                stato = "fermo"
            else:
                stato = "libero"
            reale = pag.position()
            x, y = self.puntatore.aggiorna(
                punta.x, punta.y, t, self.precisione, stato, (reale[0], reale[1])
            )
            self._muovi(x, y)
        else:
            self.puntatore.reset()

        # --- Click destro ---
        if pinch_dx:
            if self._sx_premuto:
                pag.mouseUp(button="left", _pause=False)
                self._sx_premuto = False
            self._sx_inizio = None
            if self._dx_inizio is None:
                self._dx_inizio = t
            elif not self._dx_eseguito and t - self._dx_inizio >= cfg.conferma_destro:
                pag.click(button="right", _pause=False)
                self._dx_eseguito = True
            testo = "Pinch pollice-medio: click destro"
        else:
            self._dx_inizio = None
            self._dx_eseguito = False

        # --- Click sinistro / trascinamento ---
        if pinch_sx:
            if self._sx_inizio is None:
                self._sx_inizio = t
            elif not self._sx_premuto and t - self._sx_inizio >= cfg.conferma_sinistro:
                pag.mouseDown(button="left", _pause=False)
                self._sx_premuto = True
            testo = (
                "Trascinamento: rilascia il pinch"
                if self._sx_premuto
                else "Pinch pollice-indice: conferma click"
            )
        else:
            self._sx_inizio = None
            if self._sx_premuto:
                pag.mouseUp(button="left", _pause=False)
                self._sx_premuto = False

        self._sx_attivo = pinch_sx
        self._dx_attivo = pinch_dx

        if self.precisione:
            testo = f"Precisione attiva | {testo}"
        return testo


def _percorso_modello() -> Path:
    percorso = Path(__file__).with_name("hand_landmarker.task")
    if percorso.is_file():
        return percorso

    print("Scarico il modello per il riconoscimento della mano...")
    temporaneo: str | None = None
    try:
        with urllib.request.urlopen(URL_MODELLO, timeout=60) as risposta:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=percorso.parent, suffix=".download", delete=False
            ) as file_temporaneo:
                temporaneo = file_temporaneo.name
                while blocco := risposta.read(1024 * 1024):
                    file_temporaneo.write(blocco)
        Path(temporaneo).replace(percorso)
    except (OSError, urllib.error.URLError) as errore:
        if temporaneo is not None:
            Path(temporaneo).unlink(missing_ok=True)
        raise RuntimeError(
            "Non riesco a scaricare il modello MediaPipe. Controlla la connessione "
            "Internet e riprova."
        ) from errore

    print(f"Modello salvato in: {percorso}")
    return percorso


class Webcam:
    """Legge la webcam in un thread: il loop principale riceve sempre l'ultimo frame."""

    def __init__(self, cv2, cfg: Config) -> None:  # noqa: ANN001
        self._cv2 = cv2
        backend = cv2.CAP_DSHOW if sys.platform == "win32" else cv2.CAP_ANY
        self._cap = cv2.VideoCapture(cfg.camera_indice, backend)
        if not self._cap.isOpened():
            self._cap.release()
            raise RuntimeError(
                "Impossibile aprire la webcam. Controlla che sia collegata e non "
                "sia gia' in uso da un'altra applicazione."
            )
        self._cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg.larghezza_cam)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg.altezza_cam)
        self._cap.set(cv2.CAP_PROP_FPS, cfg.fps_cam)
        self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self._cond = threading.Condition()
        self._frame = None
        self._t = 0.0
        self._id = 0
        self._errore: str | None = None
        self._stop = False
        self._thread = threading.Thread(target=self._ciclo, daemon=True)
        self._thread.start()

    def _ciclo(self) -> None:
        while not self._stop:
            letto, frame = self._cap.read()
            t = time.monotonic()
            with self._cond:
                if not letto:
                    self._errore = "La webcam ha smesso di fornire immagini."
                    self._cond.notify_all()
                    return
                self._frame = frame
                self._t = t
                self._id += 1
                self._cond.notify_all()

    def leggi(self, ultimo_id: int, timeout: float = 2.0):
        with self._cond:
            if not self._cond.wait_for(
                lambda: self._id != ultimo_id or self._errore is not None, timeout
            ):
                raise RuntimeError("Timeout: la webcam non fornisce frame.")
            if self._errore is not None:
                raise RuntimeError(self._errore)
            return self._id, self._frame, self._t

    def chiudi(self) -> None:
        self._stop = True
        self._thread.join(timeout=1.0)
        self._cap.release()


def _carica_dipendenze():
    try:
        import cv2
        import mediapipe as mp
        import pyautogui
    except ModuleNotFoundError as errore:
        if errore.name in {"cv2", "mediapipe", "pyautogui"}:
            print(
                "Librerie mancanti. Installa i requisiti con:\n"
                "  python -m pip install opencv-python mediapipe pyautogui",
                file=sys.stderr,
            )
            raise SystemExit(1) from errore
        raise
    return cv2, mp, pyautogui


def _disegna(cv2, mp, frame, mano, w: int, h: int, cfg: Config) -> None:  # noqa: ANN001
    cv2.rectangle(
        frame,
        (int(cfg.margine_x * w), int(cfg.margine_y * h)),
        (int((1 - cfg.margine_x) * w), int((1 - cfg.margine_y) * h)),
        (90, 90, 90),
        1,
    )
    for c in mp.tasks.vision.HandLandmarksConnections.HAND_CONNECTIONS:
        a, b = mano[c.start], mano[c.end]
        cv2.line(
            frame,
            (int(a.x * w), int(a.y * h)),
            (int(b.x * w), int(b.y * h)),
            (100, 180, 220),
            2,
        )
    for p in mano:
        cv2.circle(frame, (int(p.x * w), int(p.y * h)), 4, (230, 230, 230), -1)
    punta = mano[INDICE_PUNTA]
    cv2.circle(frame, (int(punta.x * w), int(punta.y * h)), 12, (80, 230, 170), -1)


def main() -> None:
    cv2, mp, pyautogui = _carica_dipendenze()
    cfg = Config()

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0
    pyautogui.MINIMUM_DURATION = 0
    pyautogui.MINIMUM_SLEEP = 0

    opzioni = mp.tasks.vision.HandLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(_percorso_modello())),
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_hands=1,
        min_hand_detection_confidence=0.65,
        min_hand_presence_confidence=0.65,
        min_tracking_confidence=0.6,
    )

    controllo = ControlloMouse(cfg, pyautogui)
    camera = Webcam(cv2, cfg)
    ultimo_id = -1
    timestamp_precedente = 0
    fps = 0.0
    t_frame_prec: float | None = None

    try:
        with mp.tasks.vision.HandLandmarker.create_from_options(opzioni) as mani:
            while True:
                ultimo_id, grezzo, t_cattura = camera.leggi(ultimo_id)
                fotogramma = cv2.flip(grezzo, 1)
                altezza_video, larghezza_video = fotogramma.shape[:2]
                rgb = cv2.cvtColor(fotogramma, cv2.COLOR_BGR2RGB)
                immagine = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
                timestamp_ms = max(timestamp_precedente + 1, int(t_cattura * 1000))
                timestamp_precedente = timestamp_ms
                risultato = mani.detect_for_video(immagine, timestamp_ms)

                if risultato.hand_landmarks:
                    mano = risultato.hand_landmarks[0]
                    _disegna(cv2, mp, fotogramma, mano, larghezza_video, altezza_video, cfg)
                    if controllo.pausa:
                        testo = "PAUSA (P per riprendere)"
                    else:
                        testo = controllo.elabora(
                            mano, t_cattura, larghezza_video, altezza_video
                        )
                else:
                    controllo.mano_persa(t_cattura)
                    testo = "PAUSA (P per riprendere)" if controllo.pausa else (
                        "Mostra la mano alla webcam"
                    )

                ora = time.monotonic()
                if t_frame_prec is not None:
                    fps = 0.9 * fps + 0.1 / max(ora - t_frame_prec, 1e-3)
                t_frame_prec = ora
                latenza_ms = (ora - t_cattura) * 1000

                cv2.putText(
                    fotogramma, testo, (16, 32), cv2.FONT_HERSHEY_SIMPLEX,
                    0.58, (240, 245, 250), 2, cv2.LINE_AA,
                )
                cv2.putText(
                    fotogramma, f"{fps:4.1f} FPS | {latenza_ms:4.0f} ms",
                    (16, 56), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (160, 220, 160), 1, cv2.LINE_AA,
                )
                cv2.putText(
                    fotogramma,
                    "Q/ESC esci | P pausa | Pinch indice: click/trascina | "
                    "Pinch medio: destro | 2 dita: scroll | 3 dita: precisione",
                    (16, altezza_video - 18), cv2.FONT_HERSHEY_SIMPLEX,
                    0.40, (240, 245, 250), 1, cv2.LINE_AA,
                )
                cv2.imshow("Controllo mouse con l'indice", fotogramma)

                tasto = cv2.waitKey(1) & 0xFF
                if tasto in (ord("q"), 27):
                    break
                if tasto == ord("p"):
                    controllo.alterna_pausa()
    except pyautogui.FailSafeException:
        print("Arresto di sicurezza: cursore portato nell'angolo superiore sinistro.")
    finally:
        pyautogui.FAILSAFE = False  # il rilascio del mouse non deve rilanciare il failsafe
        controllo.rilascia_tutto()
        camera.chiudi()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()