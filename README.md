# Corso di Python per Data Analyst

Repository di appunti, esercizi e piccoli progetti sviluppati durante un corso di Python orientato all'analisi dei dati e all'automazione con Excel. Gli esempi sono organizzati per argomento e pensati per essere eseguiti e modificati durante lo studio.

## Argomenti

- Fondamenti di Python: variabili, tipi di dato, condizioni, cicli e input.
- Funzioni, moduli e import; esercizi pratici e piccoli programmi interattivi.
- Lettura, scrittura e formattazione di file Excel con `openpyxl`.
- Analisi e conversione di dati con `pandas`, anche da CSV, JSON ed Excel.
- Grafici e visualizzazione con `matplotlib` e `seaborn`, con esempi che usano anche `numpy`.
- Esercizi e progetti, tra cui la generazione di file e un programma per creare report Excel.

## Struttura del repository

| Cartella o file | Contenuto |
| --- | --- |
| `Variabili_e_TDati/` | Variabili, tipi di dato, conversioni e condizioni. |
| `Pratica_1/` | Esercizi introduttivi e pratica aggiuntiva. |
| `for_loop/`, `funzioni/`, `import_lib/` | Cicli, funzioni, moduli ed esempi interattivi. |
| `excelpy/` | Esempi di lettura, modifica, formattazione e formule nei file Excel. |
| `ExcelBot/` | Programma per lavorare con dati di vendita e produrre report Excel. |
| `panda_data/` | Esempi ed esercizi di analisi e conversione dei dati con `pandas`. |
| `MatPlot/`, `Grafici/` | Grafici e analisi con `matplotlib`, `seaborn` e `numpy`. |
| `FileGen/`, `dati_gen/` | Esempi relativi alla generazione di file e dati. |
| `vendite.csv` e file nelle cartelle | Dati di esempio usati da alcuni esercizi e programmi. |

## Requisiti

È necessario Python 3. Non è presente un file `requirements.txt`: gli esempi introduttivi usano solo la libreria standard, mentre quelli di analisi e Excel possono richiedere `pandas`, `matplotlib`, `seaborn`, `numpy` e `openpyxl`.

Per installare le librerie usate dagli esempi:

```powershell
python -m pip install pandas matplotlib seaborn numpy openpyxl
```

## Esecuzione

Ogni file Python è un esempio autonomo: apri il progetto nell'editor e avvia lo script che vuoi provare. Per esempio, da PowerShell nella cartella principale del repository:

```powershell
python .\Variabili_e_TDati\tipi_di_dati.py
```

Avvia gli script dalla cartella principale quando leggono file di dati tramite percorsi relativi. Alcuni esempi scrivono o modificano file: controlla il codice e i percorsi utilizzati prima di eseguirli.
