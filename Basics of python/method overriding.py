#base class
# class User:
#
#    def getinfo(self):
#      print("Learn Python")
#
# #Derived Class
# class Employees(User):
#
#    def getinfo(self):
#      print("Welcome to Python")
#
# e1 = Employees()
# e1.getinfo()



class Base():

    # Constructor
    def __init__(self, x):
        self.x = x

    def sample(self):
        print("Hello base")

class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        super(Derived, self).__init__(x)
        self.y = y
        super(Derived, self).sample()

    def sample(self):
        print("Hello derived")

    def printXY(self):

    # Note that Base.x won't work here
    # because super() is used in constructor
        print(self.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()
#d.sample()