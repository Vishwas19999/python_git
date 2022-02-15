class movie:
    def __init__(self,name,actor):
        self._name=name
        self.actor=actor

    def description(self):
        return f"the movie {self._name} has acted by {self.actor}"

obj=movie("Don","SRK")

#print(obj.description())
print(obj._name)
print(obj.actor)

class car:
     def __init__(self, name, model):
         self.name = name
         self.__model = model

     def description(self):
        return f"the car {self.name} is a {self.__model} model"

obj=car("Jaguar","XF 2022")
print(obj.name)
print(obj._car__model)
#print(obj.description())

