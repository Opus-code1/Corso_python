"""Modulo ExcelBot.

Questo script legge un file Excel contenente dati di vendita, calcola il totale
per ogni riga, crea un report formattato e salva il risultato in un nuovo file.

Flusso principale del programma:
1. Leggere il file Excel di origine.
2. Filtrare le righe valide e ignorare eventuali celle vuote.
3. Calcolare il totale per ogni prodotto (prezzo x quantità).
4. Creare un nuovo file Excel con intestazione, stili e formula del totale finale.
5. Salvare il report in una cartella di output.

Documentazione:
- leggi_vendite(percorso): legge i dati dal file Excel.
- calcolo_totali(dati): aggiunge la colonna Totale a ciascuna riga.
- crea_report(dati_con_tot, percorso_output): genera il file Excel finale.
"""

# =====================================================
# IMPORTAZIONI
# =====================================================

# Importa la classe Workbook per creare e gestire file Excel.
from openpyxl import Workbook, load_workbook

# Importa gli stili usati per formattare le celle del report.
from openpyxl.styles import Font, PatternFill, Alignment

# Importa il modulo os per controllare se il file esiste e gestire percorsi.
import os


# =====================================================
# FUNZIONI
# =====================================================

# Definizione della funzione che legge i dati di vendita da un file Excel.
def leggi_vendite(percorso):
    """Legge i dati di vendita da un file Excel.

    La funzione verifica che il percorso esista, apre il file e legge tutte le
    righe a partire dalla seconda riga (salto dell'intestazione). Restituisce
    una lista di tuple contenenti i dati delle vendite.

    Args:
        percorso (str): Percorso completo o relativo del file Excel di origine.

    Returns:
        list: Lista di tuple con i dati letti dal file. Se il file non esiste o
        non contiene fogli validi, restituisce una lista vuota.
    """
    # Controlla se il file specificato esiste nel percorso indicato.
    if not os.path.exists(percorso):
        # Stampa un messaggio di errore se il file non viene trovato.
        print(f"ERRORE: il file {percorso} non esiste")
        # Restituisce una lista vuota per evitare errori nel flusso principale.
        return []

    # Carica il file Excel dal percorso fornito.
    wb = load_workbook(percorso)
    # Seleziona il foglio attivo del workbook.
    ws = wb.active

    # Verifica che il foglio attivo esista e sia valido.
    if ws is None:
        # Avvisa l'utente se il workbook non contiene fogli validi.
        print(f"ERRORE: il file {percorso} non contiene fogli validi")
        # Restituisce una lista vuota.
        return []

    # Inizializza una lista vuota dove verranno salvati i dati letti.
    dati = []

    # Scorre tutte le righe del foglio, partendo dalla seconda riga,
    # e ottiene i valori senza includere il riferimento alle celle.
    for riga in ws.iter_rows(min_row=2, values_only=True):
        # Salta eventuali righe dove la prima cella è vuota.
        if riga[0] is not None:
            # Aggiunge la riga letta alla lista dei dati.
            dati.append(riga)

    # Restituisce la lista di righe con i dati delle vendite.
    return dati


# Definizione della funzione che aggiunge la colonna Totale a ogni vendita.
def calcolo_totali(dati):
    """Calcola il totale di ogni riga di vendita.

    Ogni riga del dataset è composta da prodotto, prezzo e quantità. La funzione
    moltiplica prezzo per quantità e crea una nuova tupla con il risultato.

    Args:
        dati (list): Lista di tuple con struttura (prodotto, prezzo, quantità).

    Returns:
        list: Lista di tuple con struttura (prodotto, prezzo, quantità, totale).
    """
    # Inizializza la lista che conterrà i dati completi con il totale.
    risultati = []

    # Cicla su ogni riga ricevuta come parametro.
    for riga in dati:
        # Estrae i valori principali della riga.
        prodotto = riga[0]
        prezzo = riga[1]
        quantita = riga[2]

        # Calcola il totale della vendita.
        totale = prezzo * quantita

        # Crea una nuova tupla con prodotto, prezzo, quantità e totale.
        nuova_riga = (prodotto, prezzo, quantita, totale)

        # Aggiunge la riga con il totale alla lista dei risultati.
        risultati.append(nuova_riga)

    # Restituisce la lista finale con i totali calcolati.
    return risultati


# Definizione della funzione che crea il report finale in un nuovo file Excel.
def crea_report(dati_con_tot, percorso_output):
    """Genera un report Excel formattato con i totali e il totale finale.

    La funzione crea un nuovo workbook, aggiunge l'intestazione, applica stili,
    inserisce i dati ricevuti, calcola il totale aggregato della colonna D e salva
    il file Excel nel percorso specificato.

    Args:
        dati_con_tot (list): Lista di tuple con dati già completi del totale.
        percorso_output (str): Percorso del file Excel da creare.

    Returns:
        None: Il file viene salvato sul disco e la funzione stampa il messaggio
        di conferma.
    """
    # Crea un nuovo workbook vuoto.
    wb = Workbook()
    # Seleziona il foglio attivo del nuovo workbook.
    ws = wb.active

    # Verifica che il foglio sia stato creato correttamente.
    if ws is None:
        # Genera un errore nel caso in cui il workbook non abbia un foglio attivo.
        raise ValueError("Il workbook non contiene un foglio valido")

    # Assegna un nome al foglio Excel.
    ws.title = "Report"

    # Definisce le intestazioni della tabella.
    intestazione = ['Prodotto', 'Prezzo', 'Quantità', 'Totale']
    # Scrive la riga delle intestazioni nel foglio.
    ws.append(intestazione)

    # Imposta la larghezza delle colonne A, B, C, D.
    colori = {
        'A': 20,
        'B': 12,
        'C': 12,
        'D': 12,
    }

    # Definisce i colori per lo sfondo e il testo dell'intestazione.
    colore_sfondo = "3F41D4"
    colore_txt = "FFFFFF"

    # Crea un riempimento solido con colore di sfondo.
    riempimento = PatternFill("solid", fgColor=colore_sfondo)

    # Imposta il font in grassetto e con testo bianco per le intestazioni.
    font_intest = Font(bold=True, color=colore_txt)
    # Centra orizzontalmente il contenuto delle celle.
    allineamento = Alignment(horizontal="center")

    # Applica lo stile a tutte le celle della prima riga (intestazione).
    for cella in ws[1]:
        # Imposta il font della cella.
        cella.font = font_intest
        # Imposta il riempimento del colore di sfondo.
        cella.fill = riempimento
        # Centra il testo nella cella.
        cella.alignment = allineamento

    # Imposta la larghezza di ciascuna colonna in base alla mappa colori.
    for colonna, larghezza in colori.items():
        ws.column_dimensions[colonna].width = larghezza

    # Aggiunge tutte le righe di vendita con i totali calcolati al report.
    for riga in dati_con_tot:
        ws.append(riga)

    # Determina l'ultima riga presente nel foglio dopo l'aggiunta dei dati.
    ultima_riga = ws.max_row
    # Calcola la riga dove verrà inserito il totale finale.
    riga_totale = ultima_riga + 1

    # Inserisce la label "TOTALE" nella colonna A della riga finale.
    ws[f"A{riga_totale}"] = "TOTALE"
    # Inserisce la formula che somma tutti i valori presenti nella colonna D
    # a partire dalla seconda riga fino all'ultima riga dei dati.
    ws[f"D{riga_totale}"] = f"=SUM(D2:D{ultima_riga})"
    # Applica il carattere grassetto alla cella del totale e alla label.
    ws[f"A{riga_totale}"].font = Font(bold=True)
    ws[f"D{riga_totale}"].font = Font(bold=True)

    # Salva il workbook nel percorso specificato.
    wb.save(percorso_output)
    # Stampa un messaggio di conferma con il percorso del file generato.
    print(f"File salvato in: {percorso_output}")


# =====================================================
# ESECUZIONE PRINCIPALE
# =====================================================

# Percorso del file Excel di input contenente i dati di vendita.
file_input = "./ExcelBot/vendite.xlsx"
# Percorso del file Excel di output dove verrà salvato il report finalizzato.
file_output = "./ExcelBot/report_vendite.xlsx"

# Legge i dati dal file Excel sorgente.
dati = leggi_vendite(file_input)

# Controlla se sono stati trovati dati validi nel file.
if not dati:
    # Informa l'utente che non sono stati rilevati dati.
    print("Nessun dato è stato trovato")
else:
    # Comunica quante righe sono state lette.
    print(f"Lette {len(dati)} righe di file")
    # Calcola il totale per ogni riga di vendita.
    dati_con_totali = calcolo_totali(dati)
    # Genera il report Excel finale.
    crea_report(dati_con_totali, file_output)


# =====================================================
# DOCUMENTAZIONE RAPIDA D'USO
# =====================================================
# Questo script assume che nel file Excel di input siano presenti i dati in
# colonne con la seguente struttura:
#   Colonna A: Prodotto
#   Colonna B: Prezzo
#   Colonna C: Quantità
#
# La prima riga viene considerata come intestazione e viene saltata durante
# la lettura dei dati. Il file di output verrà creato con il nome
# "report_vendite.xlsx" e con una colonna "Totale" aggiunta automaticamente.

    