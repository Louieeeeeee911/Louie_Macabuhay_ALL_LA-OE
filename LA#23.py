LA# 23
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character can stretch every part of his body!")
        return wrapper

Luffy = AnimeCharacter("Luffy", "Gum Gum Pistol")
@Luffy.introduce
def character_intro():
    print(f"I am {Luffy.name} and I can use {Luffy.ability}.")

character_intro()
