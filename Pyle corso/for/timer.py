import time
# Timer -1 secondo
ore = int(input("ore: "))
minuti = int(input("minuti: "))
secondi = int(input("secondi: "))
totale_secondi = ore * 3600 + minuti * 60 + secondi

for tempo in range(totale_secondi, -1, -1):
    ore = tempo // 3600 #-> 60 minuti
    minuti = (tempo % 3600) // 60 #-> 60 secondi
    secondi = tempo % 60
    
    print(f"{ore:02d}:{minuti:02d}:{secondi:02d}")
    time.sleep(1)
print("tempo scaduto")





