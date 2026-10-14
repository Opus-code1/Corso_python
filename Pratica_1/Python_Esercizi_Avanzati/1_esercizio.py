'''
---Gestione di una lista di studenti---

Crea un programma che gestisca una lista di studenti. 
Utilizza classi per rappresentare gli studenti con 
attributi come: nome, cognome e voto. Gli utenti devono 
poter aggiungere, visualizzare e salvare gli studenti 
su un 'file' di testo chiamato 'studenti.txt'.
'''
#--- Inizio Codice ---

import os

class Studente:
    def __init__(self, nome, cognome, voto) -> None:
        self.nome = nome.strip().capitalize()
        self.cognome = cognome.strip().capitalize()
        self.voto = voto
    
    def __str__(self) -> str:
        return f"{self.nome} {self.cognome} - Voto {self.voto}"
    
    def __repr__(self) -> str:
        return f"Studente('{self.nome}, {self.cognome}, {self.voto}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Studente): return False
        return (self.nome.lower() == self.nome.lower() and self.cognome.lower() == self.cognome.lower())

    def to_line(self):
        return f"{self.nome};{self.cognome};{self.voto};"
    

class GestoreStudenti:
    def __init__(self, file_patch="studenti.txt") -> None:
        self.file_patch = file_patch
        self.studenti = []
        self.carica_da_file()
    
    def aggiungi_studenti(self, nome, cognome, voto):
        nuovo = Studente(nome, cognome, voto)
        if nuovo in self.studenti:
            print(f"Errore: Lo studente {nome} {cognome} è già presente nella lista")
            return False
        self.studenti.append(nuovo)
        return True
    def visualizza_studenti(self):
        if not self.studenti:
            print("Nessuno studente è presente nella lista.")
            return
        print('\n' + '=' * 50)
        print(f"{'NOME':<15}{'COGNOME':<15}{'VOTO':>10}")
        print('\n' + '=' * 50)
        
        for s in self.studenti:
            print(f"{s.nome:<15}{s.cognome:<15}{s.voto:>10}")
        print('\n' + '=' * 50)
        
        print(f'Totale: {len(self.studenti)} - Media: {float(self.media_voti())}')
    
    def media_voti(self):
        if not self.studenti: return 0.0
        somma = 0.0
        for s in self.studenti:
            somma += float(s.voto)
        return somma / len(self.studenti)
    
    def cerca_studente(self, query):
        trovati = []
        for s in self.studenti:
            if query.lower() in s.nome.lower() or query.lower() in s.cognome.lower():
                trovati.append(s)
        if not trovati:
            print(f"Risultati: {query}")
        
        else:
            print(f"Trivati: {len(trovati)} studenti")
            for s in trovati:
                print(f"• {s}")
        return trovati
    
    # === FILE DI TESTO === #
    def salva_su_file(self):
        try:
            f = open(self.file_patch, "w", encoding="utf-8")
            try:
                for s in self.studenti: f.write(s.to_line())
            finally: f.close()
        except OSError:
            print("ERRORE")

    # === CARICA FILE === #
    def carica_da_file(self):
        if not os.path.exists(self.file_patch): return

        f = open(self.file_patch, 'r', encoding="utf-8")
        for riga in f:
            riga = riga.strip()
            if not riga: 
                continue
            studente = self.crea_da_riga(riga)
            if self.studenti is not None:
                self.studenti.append(studente)
        f.close()
        
    def crea_da_riga(self, riga):
        parti = riga.split(";")
        parti = [p for p in parti if p != ""]
        if len(parti) != 3:
            print("Errore")
            return None
        nome, cognome, voto = parti
        return Studente(nome=nome, cognome=cognome, voto=voto)
    
def main():
    gestore = GestoreStudenti("studenti.txt")
    while True:
        print("=== MENU ===")
        scelta = input("1-Agiungi studente\n2-Visualizza studenti\n3-Cerca studenti\n4-Salva su file\n5-Ricarica da file\n6-Esci\n→ ").strip()
        if scelta == "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            voto = input("Voto: ")
            gestore.aggiungi_studenti(nome=nome, cognome=cognome, voto=voto)
        elif scelta == "2":
            gestore.visualizza_studenti()
        elif scelta == "3":
            query = input("Cerca studenti: ")
            gestore.cerca_studente(query=query)
        elif scelta == "4":
            gestore.salva_su_file()
        elif scelta == "5":
            gestore.carica_da_file()
        elif scelta == "6":
            break

if __name__ == "__main__": main()