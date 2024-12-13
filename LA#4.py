class character:
    def __init__(hero, name, role, HP, MP, Base_Damage):
        hero.name = name
        hero.role = role
        hero.HP = HP
        hero.MP = MP
        hero.Base_Damage = Base_Damage
    
    def __str__(hero):
        return f"{hero.name} is a {hero.role} hero"
    
    
    def describe(hero):
        print(f"{hero.name} is a {hero.role} hero")
        
hero = character("Nateman", "Marksman", 2530, 443, 110)
print(hero)
