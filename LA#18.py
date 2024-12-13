class Adebayor:
    def __init__(self, meat,dry_season, wet_season):
        self.meat = meat
        self.dry_season = dry_season
        self.wet_season = wet_season
        
    
    def __str__(self):
        return f"Ang Adebayor ko ay {self.meat}, {self.dry_season}, { self.wet_season}"
    
Adebayor_dry = Adebayor("chikin", "watir", "asin")
Adebayor2 = Adebayor("baka", "watir" , "tuyo")
Adebayor3 = Adebayor("Pork", "water" , "Onyon")
print(Adebayor_dry)
print(Adebayor2)
print(Adebayor3)
