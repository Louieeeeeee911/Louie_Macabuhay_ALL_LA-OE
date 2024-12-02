OE#4

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} with {self.attack_power} damage")
        print(f"{target.name} has only {target.health} hp left")
        if target.health <= 0:
            print(f"The {target.name} is already defeated")
        
        
Bulbasaur = Player("Bulbasaur", 45, 8)
Charmander = Player("Charmander", 39, 6)

Bulbasaur.attack(Charmander)
Charmander.attack(Bulbasaur)

while Bulbasaur.health > 0 and Charmander.health > 0:
    Bulbasaur.attack(Charmander)
    if Charmander.health <= 0:
        print(f"{Bulbasaur.name} wins!")
        break
    Charmander.attack(Bulbasaur)
    if Bulbasaur.health <= 0:
        print(f"{Charmander.name} wins!")
        break
    
    
    



        
        
        
        
        
