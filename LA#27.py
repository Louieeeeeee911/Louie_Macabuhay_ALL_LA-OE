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

class NewTurtle(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"


import structure as st

leonardo = st.Leonardo("Leonardo", "Leo")
new_turtle = st.NewTurtle("NewTurtle", "Neo")

print(leonardo.alias)
print(new_turtle.alias)
