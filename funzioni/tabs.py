def tab(num:int, xmax:int=10):
    if xmax < 0:
        return f"Errore: il numero massimo non può essere negativo"
    for t in range(xmax+1):
        r = num * t
        with open("tab.txt", "a") as f:
            f.write(f"\n{str(r)}")
    return "File salvato!"

tab(5)