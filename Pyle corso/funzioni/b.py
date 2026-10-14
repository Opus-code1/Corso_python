from a import x, y


def game():
    print(f"{x} + {y}")
    ris = int(input("= "))
    if ris == x + y:
        print("Esatto!")
    else:
        print("No")