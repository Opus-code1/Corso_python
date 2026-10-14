from openpyxl import Workbook, load_workbook

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


