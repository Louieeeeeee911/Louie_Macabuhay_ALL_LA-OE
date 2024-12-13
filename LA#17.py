class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage")
        print(f"{target.name}'s remaining health {target.health}")
        if target.health <= 0:
            print(f"The {target.name} is already defeated!!")
    def heal(self, amount):
        self.health += amount
        print(f"{self.health} healed for {amount} health. Current health: {self.health}")

Layla = Player("Layla",800,100)
Miya = Player("Miya",900,200)

Layla.attack(Layla)
Miya.attack(Miya)


while Layla.health > 0 and Miya.health > 0:
    Layla.attack(Miya)
    if Miya.health <= 0:
        print(f"{Layla.name} wins! GG!")
        break
    Miya.attack(Layla)
    if Layla.health <= 0:
        print(f"{Miya.name} wins! GGWP!")
        break
Layla.heal(200)
