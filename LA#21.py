class Adowbow:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat                #public
        self._dryseason = dry_season    #protected
        self.__wetseason = wet_season   #private
        
    def __str__(self):
        return f"Ang adobo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
        
    def may_carrot_ba(self):
        return self.__wetseason
        
    def set_carrot(self, bagong_value):
        self.__wetseason = bagong_value
    
adowbong_dry = Adowbow("chicken", "water", "asin")
adowbow2 = Adowbow("baka", "watir" , "tuyo")
adowbo3 = Adowbow("Pork", "water" , "Onyon")
adowbong_dry.set_carrot("new carrot 1")
adowbow2.set_carrot("new carrot 2")
adowbo3.set_carrot("new carrot 3")
print(adowbong_dry.may_carrot_ba())
print(adowbow2.may_carrot_ba())
print(adowbo3.may_carrot_ba())
