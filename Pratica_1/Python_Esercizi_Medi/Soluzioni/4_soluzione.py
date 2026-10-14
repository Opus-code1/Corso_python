def numeri_pari(n):
    lista_pari = [numero for numero in range(2, n+1, 2)]
    return lista_pari

# Esempio di utilizzo
limite = 10
print(f"I numeri pari fino a {limite} sono: {numeri_pari(limite)}")
