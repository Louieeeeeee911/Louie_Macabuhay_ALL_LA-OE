class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describePhone(self):
        print(f"Phone Brand: {self.model}, Phone Model: {self.brand}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
phone1= Phone("Samsung", "One Plus")
phone1.describePhone()


    
