from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl import Workbook

# Creare un nuovo foglio
wb = Workbook()
ws = wb.active

ws.title = "Titolo della Tabella"

data = [
    ["Nome", "Età", "Città"],
    ["Marco", 25, "Reggio Emilia"],
    ["Lisa", 28, "Reggio Calabria"],
    ["Sarah", 21, "Palermo"],
    ["Giulia", 24, "Catania"]
]

# Inserire i dati nel foglio
for riga in data:
    ws.append(riga)

row_num = len(data) + 1  # +1 per includere la riga dell'intestazione
tab = Table(displayName="NomeQualsiasi", ref=f"A1:C{row_num}")

# Definire lo stile della tabella
style = TableStyleInfo(name="TableStyleMedium9", 
                    showRowStripes=True,
                    showColumnStripes=True,
                    showFirstColumn=False,
                    showLastColumn=False
                    )
tab.tableStyleInfo = style

# Aggiungere la tabella al foglio
ws.add_table(tab)

# Salvare il file
wb.save("tabella.xlsx")
print('File salvato come "tabella.xlsx"')
