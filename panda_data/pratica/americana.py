'''
Scrivi una funzione che, dato in 
ingresso un valore espresso in metri, mandi 
in print l'equivalente in miglia terrestri, iarde, piedi 
e pollici. Come risolverai questo esercizio?
'''
def conv(m):
    ris = {}
    ris['miglia'] = m / 1609
    ris['iarde'] = m * 1094
    ris['piedi'] = m * 3.281
    ris['pollici'] = m * 39.37
    
    for chiave, valore in ris.items(): 
        print(f"{m} metri sono: {valore} {chiave}")

conv(35)