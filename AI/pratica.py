
```python
**Consegna**: generare liste di numeri casuali e rappresentarle con **almeno 4 grafici diversi**, usando **solo `matplotlib` e `random`** (entrambi già disponibili o installabili con `pip install matplotlib`). Niente `os`, niente `sys`, niente file, niente database.

**Tempo stimato**: 45 60 minuti | **Da consegnare**: un unico file `grafici.py`

---

## Regole

- Solo `import matplotlib.pyplot as plt` e `import random`
- Solo **funzioni**: ogni grafico è una funzione separata
- Le liste di numeri casuali si generano **dentro** le funzioni (o in una funzione dedicata)
- Niente salvataggi su file: i grafici si mostrano con `plt.show()`

## Parte 1 — Funzione base (obbligatoria)

Scrivi una funzione che genera una lista di `n` numeri casuali interi tra `min` e `max`:

```python
def genera_numeri(n, minimo, massimo):
    """Restituisce una lista di n interi casuali tra minimo e massimo."""
    # ...
```

**Suggerimento**: guarda `random.randint` nella documentazione ufficiale (non chiedere all'AI la soluzione).

Poi scrivi una funzione che genera numeri casuali **decimali** tra 0 e 1:

```python
def genera_decimali(n):
    """Restituisce una lista di n numeri casuali tra 0.0 e 1.0."""
    # ...
```

**Suggerimento**: `random.random`.

---

## Parte 2 — I quattro grafici (obbligatori)

Per ogni grafico, scrivi una funzione che:

1. genera i dati con le funzioni della Parte 1,
2. disegna il grafico,
3. aggiunge titolo, etichette degli assi e legenda (dove serve),
4. chiama `plt.show()`.

### Grafico A — Istogramma

```python
def grafico_istogramma():
    """Istogramma della distribuzione di 500 numeri casuali tra 1 e 100."""
```

- Usa `plt.hist(...)`
- Aggiungi `bins=20`
- Titolo: "Distribuzione di 500 numeri casuali"

### Grafico B — Linea

```python
def grafico_linea():
    """Grafico a linea di 50 numeri decimali casuali nell'ordine di generazione."""
```

- Asse x: indice (0, 1, 2, …), asse y: valore
- Usa `plt.plot(...)` con `marker='o'`
- Titolo: "Andamento di 50 valori casuali"

### Grafico C — Dispersione (scatter)

```python
def grafico_scatter():
    """Scatter plot di 100 punti (x, y) entrambi casuali tra 0 e 100."""
```

- Genera due liste separate con `genera_numeri(100, 0, 100)`
- Usa `plt.scatter(...)`
- Titolo: "100 punti casuali"
- Etichette: "X" e "Y"

### Grafico D — A tua scelta

Scegli **uno** tra:

- **Barre**: 5 categorie ("A", "B", "C", "D", "E") con valori casuali tra 0 e 50 → `plt.bar(...)`
- **Torta**: 4 fette con valori casuali → `plt.pie(...)` con `autopct='%1.1f%%'`
- **Due linee sullo stesso grafico**: una lista casuale e la sua "media mobile" (media dei primi k valori) → `plt.plot` due volte + `plt.legend()`

---

## Parte 3 — Menu (facoltativo ma consigliato)

Una funzione `main()` che chiede all'utente quale grafico vedere:

```python
def main():
    """Menu per scegliere quale grafico mostrare."""
    while True:
        print("1) Istogramma  2) Linea  3) Scatter  4) Extra  0) Esci")
        scelta = input("Scelta: ").strip()
        if scelta == "0":
            break
        elif scelta == "1":
            grafico_istogramma()
        # ... ecc.
```

Niente `sys.argv`, niente file: solo `input()` e `plt.show()`.

---

## Esempio di struttura del file

```python
import random
import matplotlib.pyplot as plt


def genera_numeri(n, minimo, massimo):
    """Restituisce una lista di n interi casuali tra minimo e massimo."""
    # IL TUO CODICE QUI


def genera_decimali(n):
    """Restituisce una lista di n numeri casuali tra 0.0 e 1.0."""
    # IL TUO CODICE QUI


def grafico_istogramma():
    """Istogramma della distribuzione di 500 numeri casuali tra 1 e 100."""
    # IL TUO CODICE QUI


def grafico_linea():
    """Grafico a linea di 50 numeri decimali casuali."""
    # IL TUO CODICE QUI


def grafico_scatter():
    """Scatter plot di 100 punti casuali tra 0 e 100."""
    # IL TUO CODICE QUI


def grafico_extra():
    """Grafico a barre di 5 categorie con valori casuali."""
    # IL TUO CODICE QUI


def main():
    """Menu per scegliere quale grafico mostrare."""
    while True:
        print("1) Istogramma  2) Linea  3) Scatter  4) Extra  0) Esci")
        scelta = input("Scelta: ").strip()
        if scelta == "0":
            break
        elif scelta == "1":
            grafico_istogramma()
        elif scelta == "2":
            grafico_linea()
        elif scelta == "3":
            grafico_scatter()
        elif scelta == "4":
            grafico_extra()
        else:
            print("Scelta non valida")


if __name__ == "__main__":
    main()
```

---

## Cosa consegni

Un file `grafici.py` con:

1. tutte le funzioni,
2. il `main()` che funziona,
3. una riga di commento sopra ogni funzione che dice **cosa hai imparato** scrivendola (es. `# ho capito che bins controlla il numero di colonne`).

E, fuori dal file, in un messaggio a parte, rispondi a:

- **Quale grafico è stato più difficile e perché?**
- **Cosa fa `plt.show()` esattamente?** (una frase)
- **Se generi 10.000 numeri invece di 500, l'istogramma cambia forma? Perché?**

```
```
