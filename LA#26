from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"
   
class Michaelangelo(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

class Donatello(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"
   
class Raphael(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

import oop

leonardo = oop.Leonardo("Leonardo", "Leo")
michaelangelo = oop.Michaelangelo("Michaelangelo", "Gelo")
donatello = oop.Donatello("Donatello", "Dona")
raphael = oop.Raphael("Raphael", "Paeng")

print(leonardo.alias)
print(michaelangelo.alias)
print(donatello.alias)
print(raphael.alias)
