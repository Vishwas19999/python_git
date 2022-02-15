from abc import ABC
class car(ABC):
    def __init__(self,name):
        self.name=name

        #abstarct method
    def price(self,x):
        pass
class new(car):
    def price(self,x):
        print(f"the {self.name} price is {x} crores")

obj=new("Ferrari")
obj.price(2)

from abc import ABC
class cricket(ABC):
    def __init__(self,name):
        self.name=name

    def one(self,role):
        pass

class new(cricket):
    def one(self,role):
        print(f"{self.name} is a {role}")

obj=new("MSD")
obj.one("Captain")
