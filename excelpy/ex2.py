from openpyxl import Workbook as W

wb = W()

ws = wb.active

ws.append(["Prodotto", "Prezzo", "Qunatità"])
ws.append(["Mela", 1.52, 10])
ws.append(["Kiwi", 1.12, 15])
ws.append(["Ananas", 3.99, 8])

wb.save("./excelpy/file_2.xlsx")