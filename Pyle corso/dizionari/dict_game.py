import random
# dizionario giocatore
player = {
    'name':input("Nome Giocatore: "),
    'hp':100,
    'max_hp':100,
    'attack':100,
    'defense':5,
    'potions':3,
    'gold': 0
}
nomi_nemici = [
            "Goblin", "Troll", "Demone",
            "Lupo", "Unicorno", "Ape"
                ]
name = random.choice(nomi_nemici)
hp = random.randint(50, 80)
attk = random.randint(5, 10)
defense = random.randint(1, 5)
enemy = {
    'name': name,
    'hp': hp,
    'attack':attk,
    'defense': defense,
}

print(f"Sei stato attaccato da un {enemy['name']}!\n")

while True:# player['hp'] > 0 and enemy['hp'] > 0:
    action = input("Cosa fare\n-Attacca\n-Bevi Pozione\n-Scappa\n-Shop\n-Esci\n-> ").lower()
    
    if action == "esci":
        print("______________________________")
        break
    elif action == "attacca":
        if random.random() < 0.5: # 50%
            # Calcola i danni
            damage_to_enemy = max(0, player['attack'] - enemy['defense'])
            damage_to_player = max(0, enemy['attack'] - player['defense'])
        else:
            # Calcola i danni
            damage_to_player = max(0, enemy['attack'] - player['defense'])
            damage_to_enemy = max(0, player['attack'] - enemy['defense'])
            
        # Aggiornamento HP
        enemy['hp'] -= damage_to_enemy
        player['hp'] -= damage_to_player
        if enemy['hp'] < 1:
            enemy['hp'] = 0
        print(f'Hai inflitto {damage_to_enemy} danni al {enemy["name"]}')
        print(f'Il {enemy["name"]} ti ha inflitto {damage_to_player} danni')
        
    elif action == "bevi pozione":
        if player['potions'] > 0:
            if player['hp'] >= player['max_hp']:
                player['hp'] = player['max_hp']
                print("Non hai bisogno di bere la pozione")
            else:
                player['hp'] += 20
                player['potions'] -= 1
                if player['hp'] >= player['max_hp']:
                    player['hp'] = player['max_hp']
                    
                print(f"Hai bevuto la pozione! HP ricuperati!\nAdesso hai {player['hp']}")
                print(f"Ti rimangono ancora {player['potions']} pozioni")
    
    elif action == "scappa":
        if random.random() < 0.5: #50%
            print("Sei riuscito a scappare")
            continue
        else:
            print("Il nemico ti blocca la fuga")
            damage_to_player = max(0, enemy['attack'] - player['defense'])
            player['hp'] -= damage_to_player
            print(f'Il {enemy["name"]} ti ha inflitto {damage_to_player} danni')
            
    print(f'I tuoi HP: {player["hp"]}/{player["max_hp"]}')
    print(f'HP del {enemy["name"]}: {enemy["hp"]}')
    
    # controllo del risultato
    if player['hp'] <= 0:
        print("Sei stato sconfitto!")
    elif enemy['hp'] < 1:
        enemy['hp'] = 0
        print("Hai sconfitto il nemico")
        gold = random.randint(2, 5)
        player['gold'] += gold
        xp = random.randint(5, 10)
        print(f'Hai ricevuto {gold} Gold\nin totale hai {player["gold"]} Gold')
        # ricupero hp
        player['hp'] += player['max_hp'] / 2 # +50% della vita massima
        
        if player['hp'] >= player['max_hp']:
            player['hp'] = player['max_hp']
        print(f"Vita del giocatore: {player['hp']}/{player['max_hp']}")