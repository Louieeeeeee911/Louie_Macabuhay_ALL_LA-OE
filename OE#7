#OE 7
class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def Introduce(self, func):
        def intro():
            print("Introducing...")
            func()
            print(f"This Character is amazing")
        return intro
    
Devil_Jin = TekkenCharacter("Devil Jin", "Flying Laser")
@Devil_Jin.Introduce

def character_intro():
    print(f"I am {Devil_Jin.name} and I can use {Devil_Jin.ability}")
    
character_intro()
