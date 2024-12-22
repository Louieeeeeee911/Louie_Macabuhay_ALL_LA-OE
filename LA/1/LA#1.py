LA#1
class hero():
    def __init__(self, name, role, dmg_type, health, mana, basic_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.mana = mana
        self.auto_atk_dmg = basic_dmg

    def __str__(self):
        return f"this hero is {self.dmg_type}."
    
    def describe(self):
        print(f"{self.name} is a {self.role}.")

    def heroes(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power."
    
hero_mm1 = hero("Melissa", "Marksman", "attack damage", 2460, 448, 123)
hero_fighter1 = hero("Yu Zhong", "Fighter", "attack damage", 2698, 0, 129)
hero_mid1 = hero("Xavier", "Mid", "Magic Damage", 2616, 270, 111)
hero_roam1 = hero("Estes", "Roam", "Healing", 2221, 545, 120)
hero_jungle1 = hero("Frederinn", "Jungle", "Brust Damage", 2709, 0, 126)

print(f'''{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health}
{hero_mm1.mana}
{hero_mm1.auto_atk_dmg} basic damage
{hero_mm1.dmg_type}''')
hero_mm1.describe()
print(hero_mm1)
print(hero_mm1.heroes())
print()

print(f'''{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health}
{hero_fighter1.mana}
{hero_fighter1.auto_atk_dmg} basic damage
{hero_fighter1.dmg_type}''')
hero_fighter1.describe()
print(hero_fighter1)
print(hero_fighter1.heroes())
print()

print(f'''{hero_mid1.name}
{hero_mid1.role}
{hero_mid1.health}
{hero_mid1.mana}
{hero_mid1.auto_atk_dmg} basic damage
{hero_mid1.dmg_type}''')
hero_mid1.describe()
print(hero_mid1)
print(hero_mid1.heroes())
print()

print(f'''{hero_roam1.name}
{hero_roam1.role}
{hero_roam1.health}
{hero_roam1.mana}
{hero_roam1.auto_atk_dmg} basic damage
{hero_roam1.dmg_type}''')
hero_roam1.describe()
print(hero_roam1)
print(hero_roam1.heroes())
print()

print(f'''{hero_jungle1.name}
{hero_jungle1.role}
{hero_jungle1.health}
{hero_jungle1.mana}
{hero_jungle1.auto_atk_dmg} basic damage
{hero_jungle1.dmg_type}''')
hero_jungle1.describe()
print(hero_jungle1)
print(hero_jungle1.heroes())
print()
