from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill



# Salviamo tutte le fuznioni della classe
wb = Workbook()

# attivare le modifiche del file
foglio = wb.active

# Aggiungere i dati al file xlsx
foglio['A1'] = "Nome"
foglio['B1'] = "Età"
foglio['C1'] = "Città"

# aggiungere i dati al foglio
foglio.append(["Roman", 27,'Padova'])
foglio.append(['Zelda', 26, 'Roma'])
foglio.append(['Miriam', 28, 'RC'])

# Salvare il foglio xlsx
wb.save('foglio.xlsx')
print("Salvato!")

# Modificare una cella
wb = load_workbook("foglio.xlsx")
mod = wb.active
mod["A2"] = 'Sarah'

# Salvare il foglio xlsx
wb.save('foglio.xlsx')
print("Salvato!")

# Aggiungere più fogli

for i in range(5):
    wb.create_sheet("foglio_"+str(i+1))
wb.save("foglio.xlsx")
print("Salvato!")

# Selezionare il foglio specifico

f = wb.create_sheet("Dati")
f_2 = wb["Dati"]
f_2.append(['Nome','Età','Città','Stipendio','Animali'])

wb.save("foglio.xlsx")
print("Salvato!")

# ELiminare un foglio
wb.remove(wb["foglio_1"])
wb.save("foglio.xlsx")
print("Salvato!")

stile = wb.active
# Bold font
stile["A1"].font = Font(b=True)

#Cambio colore della cella
fill = PatternFill(start_color='D400FF', end_color='FFFF00', fill_type='solid')
stile['A2'].fill = fill
wb.save("foglio.xlsx")
print("Salvato!")

# Rinominare un foglio
stile.title = "Nuovo Nome"

wb.save("foglio.xlsx")
print("Salvato!!")

# Unire le celle
stile.merge_cells("A1:B1")
wb.save("foglio.xlsx")
print("Salvato!!")

# Dividere le celle
stile.unmerge_cells("A1:B1")
wb.save("foglio.xlsx")
print("Salvato!!")

















