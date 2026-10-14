# === PRATICA MEDIO 2 === #
'''
• Crea una variabile numerica chiamata "voto"

• Verifica se la variabile è uguale a 100
    • Usa la funzione print() per tampare "Sei stato promosso a pieni voti"

• Verifica se la variabile è maggiore o uguale a 60
    • Usa la funzione print() per tampare "Sei stato promosso"

• Verifica se la variabile è minore di 60
    • Usa la funzione print() per tampare "Sei stato bocciato"
'''
# === CODICE === #
voto = 59  # Puoi cambiare questo valore per testare diverse condizioni

if voto == 100:
    print("Sei stato promosso a pieni voti")
elif voto >= 60:
    print(f"Sei stato promosso con {voto}")
else:
    print("Sei stato bocciato")