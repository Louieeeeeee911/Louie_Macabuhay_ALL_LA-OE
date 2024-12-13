class character:
    def __init__(hero, name, HP, MP, Base_Damage):
        hero.name = name
        hero.HP = HP
        hero.MP = MP
        hero.Base_Damage = Base_Damage
        
hero = character("Nateman", 2530, 443, 110)
print(f'''{hero.name} 
HP: {hero.HP}
MP: {hero.MP} 
Base Damage: {hero.Base_Damage}
''')
