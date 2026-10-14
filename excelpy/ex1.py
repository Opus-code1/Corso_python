# pip install openpyxl

from openpyxl import Workbook

# creo un nuovo file
wb = Workbook()

# Prendo il foglio attivo (come quello che vedi in excel)
foglio = wb.active

# Diamo un titolo al foglio di lavoro
foglio.title = "Vendite"

foglio["A1"] = "Prodotto"
foglio["B1"] = "Prezzo"
foglio["C1"] = "Quantità"

# scrivo dei dati
foglio['A2'] = "Telefono"
foglio['B2'] = 449.99 
foglio['C2'] = 15

foglio['A3'] = "Computer"
foglio['B3'] = 1449.99 
foglio['C3'] = 52

foglio['A4'] = "Cuffie"
foglio['B4'] = 55
foglio['C4'] = 7

# "C:\\Users\\avare\\Desktop\\Pyhton\\excelpy\\vendite.xlsx"
wb.save("./excelpy/vendite.xlsx")

'''
• Workbook() → crea un file Excel in memoria (non fisico)
• wb.active → il nostro voglio attuale
• wb.save() → salva il foglio
'''

