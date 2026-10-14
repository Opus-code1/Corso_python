import time

tempo = int(input("secondi: "))
for i in range(tempo, 0, -1):
    print(i)
    time.sleep(1)
print("Tempo scaduto")