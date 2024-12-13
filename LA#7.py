class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car1 = car("Lambo","Red")
print(car1.brand)
print(car1.color)
car1.color = "Black"
print(car1.color)
