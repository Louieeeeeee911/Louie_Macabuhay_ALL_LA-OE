# LA#22
class Party:
    def __init__(self, name):
        self.name = name
    def __secret(self):
        print(f"Secret Dish: {self.name}")
        
    def foods(self):
        print(f"{self.name} party: Wine, Baby oil, Coke, JB, LJ, Usher")
        print("Special Dish: Diddy, Beyonce, Jay-Z")
        self.__secret()

Diddy = Party("Diddy")
Beach = Party("Beach")
Bday = Party("Bday")
Diddy.foods()
Beach.foods()
Bday.foods()
