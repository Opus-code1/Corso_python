import numpy as np
import sounddevice as sd
import psutil
import time
# variabili
b_min = 25 # min %
b_max = 80 # max %
# parametri del suono
duration = 0.5 # durata del suono
sample_rate = 45000 # frequenza di campionamento in HZ

# frequenza dei suoni
freq_high = 400 # Batteria Carica
freq_low = 600 # Batteria Scarica
freq_med = 800 # Batteria Assente

# Stato precedente della batteria per evitare il suono in loop
previous_state = None

# bool
can_min = True
can_max = True


# Generatore di suono
def generatore_suono(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    return waveform

# Controllare lo stato della batteria
def battery_check():
    global battery, previous_state, can_min, can_max
    # gestione errori
    try:
        # prova a monitorare la mia batteria
        battery = psutil.sensors_battery()
    except Exception as e:
        print(f"Errore: {e}")
        return
    
    # Se la batteria è presente nel computer
    if battery is not None:
        # Percentuale della batteria minore al minimo
        if battery.percent < b_min and previous_state != "low" and can_min:
            can_min = False
            waveform = generatore_suono(freq_low, duration, sample_rate)
            for i in range(3):
                sd.play(waveform, sample_rate)
                sd.wait()
            previous_state = 'low'
        # Percentuale della batteria maggiore o uguale al massimo
        elif battery.percent >= b_max and previous_state != 'high' and can_max:
            can_max = False
            waveform = generatore_suono(freq_low, duration, sample_rate)
            for i in range(3):
                sd.play(waveform, sample_rate)
                sd.wait()
            previous_state = 'high'
        # Percentuale della batteria media tra il minimo e il massimo
        elif battery.percent >= b_min and battery.percent < b_max:
            previous_state = None

while True:
    battery_check()
    if battery.percent > b_min:
        can_min = True
    
    if battery.percent < b_max:
        can_max = True
    
    time.sleep(1)





