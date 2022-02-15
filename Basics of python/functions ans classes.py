class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

emp=employee('vishu',22)
print(emp.name)
print(emp.age)

class student:
    def __init__(self,name,clg):
        self.name=name
        self.clg=clg

    def new(self):
        print(' hi my name is ' + self.name)
        print(' my clg is ' + self.clg)

std=student('vishwas','Vidhyadri')
std.new()


class company:
    def __init__(self,name,location):
        self.name=name
        self.location=location

    def my(self):
        print(" My company name is " + self.name)
        print(" Location is " + self.location)

com=company("GOOGLE","CALIFORNIA")
com.my()








