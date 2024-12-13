class Spiderman():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def describeSpiderman(self):
        print (f"Name: {self.name} Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self,name,age,movie):
        super().__init__(name,age)
        self.movie = movie
        
class Andrew(Spiderman):
    def __init__(self,name,age,movie):
        super().__init__(name, age)
        self.movie = movie

class Tom(Spiderman):
    def __init__(self,name,age,movie):
        super().__init__(name,age)
        self.movie = movie
        
Maguire = Tobey("Tobey Maguire", "49", "Venom")
Garfield = Andrew("Andrew Garfield", "41", "The Amazing Spiderman 2")
Holland = Tom("Tom Holland", "28", "Avengers End Game")

print(f"Name: {Maguire.name.upper()}, Movie: {Maguire.movie}")
print(f"Name: {Garfield.name.upper()}, Movie: {Garfield.movie}")
print(f"Name: {Holland.name.upper()}, Movie: {Holland.movie}")




        
