import requests

link = "https://www.randomuser.me/api"

risposta = requests.get(link)

def status(debug=False):
    ok: bool
    ok = True if risposta.status_code == 200 else False
    if debug: print(f"Staus Code: {risposta.status_code}")
    return ok

def save(file="data.json", data=""):
    with open(file, "w", encoding='utf-8') as f:
        f.write(str(data))

if status():
    data = risposta.json()
    # save(file="./REQUEST/dati_random.json", data=data)
    
    user = data['results'][0]
    nome = user['name']['first']
    cognome = user['name']['last']
    anni = user['dob']['age']
    anno = user['dob']['date']
    
    persona = f"Ciao, mi chiamo {nome} {cognome}, sono nata/o nel {anno} e ho {anni} anni"
    print()
    print(persona)
    print()


