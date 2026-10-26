import random
import tkinter as tk
from tkinter import ttk
from typing import Callable

from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


SFONDO = "#202830"
PANNELLO = "#2b3641"
TESTO = "#edf2f7"
TESTO_SECONDARIO = "#aebbc8"
ACCENTO = "#39b8a5"
COLORI_GRAFICI = ("#39b8a5", "#f2b45e", "#70a7e8", "#d184c5")


def genera_numeri(n: int, minimo: int, massimo: int) -> list[int]:
    """Restituisce una lista di n interi casuali tra minimo e massimo."""
    return [random.randint(minimo, massimo) for _ in range(n)]


def genera_decimali(n: int) -> list[float]:
    """Restituisce una lista di n numeri casuali tra 0.0 e 1.0."""
    return [random.random() for _ in range(n)]


def _crea_figura(titolo: str, asse_x: str, asse_y: str) -> tuple[Figure, Axes]:
    figura = Figure(figsize=(7, 4.5), facecolor=SFONDO, tight_layout=True)
    asse = figura.add_subplot(111)
    asse.set_facecolor(PANNELLO)
    asse.set_title(titolo, color=TESTO, pad=14)
    asse.set_xlabel(asse_x, color=TESTO_SECONDARIO)
    asse.set_ylabel(asse_y, color=TESTO_SECONDARIO)
    asse.tick_params(colors=TESTO_SECONDARIO)
    asse.grid(axis="y", color="#52606d", alpha=0.35, linestyle="--")
    for bordo in asse.spines.values():
        bordo.set_color("#52606d")
    return figura, asse


def grafico_istogramma() -> Figure:
    """Crea un istogramma di 500 numeri casuali tra 1 e 100."""
    numeri = genera_numeri(500, 1, 100)
    figura, asse = _crea_figura(
        "Distribuzione di 500 numeri casuali", "Valore", "Frequenza"
    )
    asse.hist(
        numeri,
        bins=20,
        color=COLORI_GRAFICI[0],
        edgecolor=SFONDO,
        label="Numeri casuali",
    )
    asse.legend(facecolor=PANNELLO, edgecolor="#52606d", labelcolor=TESTO)
    return figura


def grafico_linea() -> Figure:
    """Crea un grafico a linea con 50 numeri decimali casuali."""
    valori = genera_decimali(50)
    indici = list(range(len(valori)))
    figura, asse = _crea_figura("Andamento di 50 valori casuali", "Indice", "Valore")
    asse.plot(
        indici,
        valori,
        marker="o",
        markersize=4,
        color=COLORI_GRAFICI[1],
        label="Valori casuali",
    )
    asse.legend(facecolor=PANNELLO, edgecolor="#52606d", labelcolor=TESTO)
    return figura


def grafico_scatter() -> Figure:
    """Crea un grafico scatter con 100 punti casuali."""
    valori_x = genera_numeri(100, 0, 100)
    valori_y = genera_numeri(100, 0, 100)
    figura, asse = _crea_figura("100 punti casuali", "X", "Y")
    asse.scatter(
        valori_x,
        valori_y,
        color=COLORI_GRAFICI[2],
        alpha=0.8,
        label="Punti casuali",
    )
    asse.legend(facecolor=PANNELLO, edgecolor="#52606d", labelcolor=TESTO)
    return figura


def grafico_extra() -> Figure:
    """Crea un grafico a barre con cinque categorie casuali."""
    categorie = ["A", "B", "C", "D", "E"]
    valori = genera_numeri(5, 0, 50)
    figura, asse = _crea_figura("Valori casuali per categoria", "Categoria", "Valore")
    asse.bar(
        categorie,
        valori,
        color=COLORI_GRAFICI[3],
        label="Valori casuali",
    )
    asse.legend(facecolor=PANNELLO, edgecolor="#52606d", labelcolor=TESTO)
    return figura


GRAFICI: tuple[tuple[str, str, str, Callable[[], Figure]], ...] = (
    (
        "istogramma",
        "Istogramma",
        "Distribuzione di 500 numeri casuali",
        grafico_istogramma,
    ),
    ("linea", "Grafico a linea", "Andamento di 50 valori casuali", grafico_linea),
    ("scatter", "Scatter", "Relazione tra 100 coppie di valori", grafico_scatter),
    ("barre", "Grafico a barre", "Confronto tra cinque categorie", grafico_extra),
)


class MenuGrafici(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Esplora i grafici")
        self.configure(background=SFONDO)
        self.geometry("720x650")
        self.minsize(600, 560)
        self.finestre_grafici: dict[str, tk.Toplevel] = {}
        self.selezioni = {chiave: tk.BooleanVar(value=False) for chiave, *_ in GRAFICI}
        self.stato = tk.StringVar()

        self._configura_stile()
        self._crea_interfaccia()
        self._aggiorna_stato()

    def _configura_stile(self) -> None:
        stile = ttk.Style(self)
        stile.theme_use("clam")
        stile.configure(
            ".",
            background=SFONDO,
            foreground=TESTO,
            font=("Segoe UI", 10),
        )
        stile.configure("TFrame", background=SFONDO)
        stile.configure("Panel.TFrame", background=PANNELLO)
        stile.configure("TLabel", background=SFONDO, foreground=TESTO)
        stile.configure("Muted.TLabel", background=SFONDO, foreground=TESTO_SECONDARIO)
        stile.configure(
            "CardTitle.TLabel",
            background=PANNELLO,
            foreground=TESTO,
            font=("Segoe UI Semibold", 11),
        )
        stile.configure(
            "TCheckbutton",
            background=PANNELLO,
            foreground=TESTO,
            padding=(10, 12),
        )
        stile.map(
            "TCheckbutton",
            background=[("active", "#34424e")],
            foreground=[("disabled", TESTO_SECONDARIO)],
        )
        stile.configure(
            "Accent.TButton",
            background=ACCENTO,
            foreground="#12201f",
            padding=(14, 10),
            font=("Segoe UI Semibold", 10),
            borderwidth=0,
        )
        stile.map(
            "Accent.TButton",
            background=[("active", "#56cbb9"), ("disabled", "#52606d")],
            foreground=[("disabled", "#c3cbd2")],
        )
        stile.configure("TButton", padding=(10, 7))

    def _crea_interfaccia(self) -> None:
        contenitore = ttk.Frame(self, padding=(28, 24))
        contenitore.pack(fill="both", expand=True)

        ttk.Label(
            contenitore,
            text="Esplora i grafici",
            font=("Segoe UI Semibold", 22),
        ).pack(anchor="w")
        ttk.Label(
            contenitore,
            text="Scegli uno o più grafici da visualizzare. Ogni tipo compare una sola volta.",
            style="Muted.TLabel",
            wraplength=620,
        ).pack(anchor="w", pady=(5, 22))

        ttk.Label(
            contenitore,
            text="GRAFICI DISPONIBILI",
            style="Muted.TLabel",
            font=("Segoe UI Semibold", 9),
        ).pack(anchor="w", pady=(0, 9))

        elenco = ttk.Frame(contenitore)
        elenco.pack(fill="x")
        for chiave, nome, descrizione, _ in GRAFICI:
            scheda = ttk.Frame(elenco, style="Panel.TFrame", padding=(6, 3))
            scheda.pack(fill="x", pady=5)
            testo = ttk.Frame(scheda, style="Panel.TFrame")
            testo.pack(side="left", fill="x", expand=True)
            ttk.Label(testo, text=nome, style="CardTitle.TLabel").pack(
                anchor="w", padx=10, pady=(7, 1)
            )
            ttk.Label(
                testo,
                text=descrizione,
                background=PANNELLO,
                foreground=TESTO_SECONDARIO,
            ).pack(anchor="w", padx=10, pady=(0, 7))
            ttk.Checkbutton(
                scheda,
                text="Seleziona",
                variable=self.selezioni[chiave],
                command=self._aggiorna_stato,
            ).pack(side="right", padx=6)

        comandi = ttk.Frame(contenitore)
        comandi.pack(fill="x", pady=(14, 0))
        ttk.Button(
            comandi,
            text="Apri grafici selezionati",
            style="Accent.TButton",
            command=self._apri_selezionati,
        ).pack(side="left")
        ttk.Button(comandi, text="Seleziona tutti", command=self._seleziona_tutti).pack(
            side="left", padx=(10, 0)
        )
        ttk.Button(comandi, text="Deseleziona", command=self._deseleziona_tutti).pack(
            side="left", padx=(8, 0)
        )

        ttk.Separator(contenitore).pack(fill="x", pady=(22, 12))
        ttk.Label(contenitore, textvariable=self.stato, style="Muted.TLabel").pack(
            anchor="w"
        )

    def _seleziona_tutti(self) -> None:
        for selezione in self.selezioni.values():
            selezione.set(True)
        self._aggiorna_stato()

    def _deseleziona_tutti(self) -> None:
        for selezione in self.selezioni.values():
            selezione.set(False)
        self._aggiorna_stato()

    def _apri_selezionati(self) -> None:
        selezionati = [
            (chiave, nome, crea_grafico)
            for chiave, nome, _, crea_grafico in GRAFICI
            if self.selezioni[chiave].get()
        ]
        if not selezionati:
            self.stato.set("Seleziona almeno un grafico per continuare.")
            return

        for chiave, nome, crea_grafico in selezionati:
            finestra = self.finestre_grafici.get(chiave)
            if finestra is not None and finestra.winfo_exists():
                finestra.deiconify()
                finestra.lift()
                finestra.focus_set()
                continue

            finestra = tk.Toplevel(self)
            finestra.title(nome)
            finestra.configure(background=SFONDO)
            finestra.geometry("800x570")
            self.finestre_grafici[chiave] = finestra

            figura = crea_grafico()
            canvas = FigureCanvasTkAgg(figura, master=finestra)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, finestra, pack_toolbar=False)
            toolbar.update()
            toolbar.pack(side="bottom", fill="x")
            canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

            def chiudi_finestra(
                grafico: str = chiave,
                finestra_corrente: tk.Toplevel = finestra,
            ) -> None:
                if self.finestre_grafici.get(grafico) is finestra_corrente:
                    del self.finestre_grafici[grafico]
                finestra_corrente.destroy()

            finestra.protocol("WM_DELETE_WINDOW", chiudi_finestra)

        self._aggiorna_stato()

    def _aggiorna_stato(self) -> None:
        selezionati = sum(selezione.get() for selezione in self.selezioni.values())
        aperti = sum(finestra.winfo_exists() for finestra in self.finestre_grafici.values())
        self.stato.set(f"{selezionati} selezionati  |  {aperti} finestre grafico aperte")


def main() -> None:
    """Avvia il menu grafico."""
    applicazione = MenuGrafici()
    applicazione.mainloop()


if __name__ == "__main__":
    main()
