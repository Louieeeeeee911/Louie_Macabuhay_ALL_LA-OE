class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describeToy(self):
        print(f"Toy Name: {self.name} \nToy Price: {self.price}\n")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
laruan = Car("Rose", "$99.9")
laruan.describeToy()
