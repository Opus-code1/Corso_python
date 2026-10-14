# === MENU === #
primi_piatti = {
    'carbonara': 3.99,
    'lasagna': 5.58,
    'wurstel': 2.99,
    'kebab': 4.99,
    'aglio olio e peperoncino': 9.99,
    'tortellini': 5.42
    }

bibite = {
    'monster': 1.69,
    'chinotto': 4.98,
    'fanta': 2.58,
    'cola': 3.57,
    'pepsi': 2.36,
    'acqua': 1.25
    }

def primi():
    print("=== PRIMI PIATTI ===")
    for p, c in primi_piatti.items():
        print(f"{p}: €{c}")

def bevande():
    print("=== BEVANDE ===")
    for p, c in bibite.items():
        print(f"{p}: €{c}")

if __name__ == "__main__":
    print(primi_piatti)
    print(bibite)
    primi()
    bevande()