import time

ore = 0
minuti = 0
secondi = 0

while True:
    print(f"{ore:02d}:{minuti:02d}:{secondi:02d}")
    time.sleep(1)
    
    secondi += 1
    
    if secondi == 60:
        secondi = 0
        minuti += 1
    
    if minuti == 60:
        minuti = 0
        ore += 1
    




