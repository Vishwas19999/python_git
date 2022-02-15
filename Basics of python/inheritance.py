class employee():
    empname=" "
    def new1(self):
        print(self.empname)

class department():
    location=" "
    def new2(self):
        print(self.location)

class admin(employee,department):
    def new3(self):
        print("employee:",self.empname)
        print("department:",self.location)
obj=admin()
obj.name="Vishu"
obj.location="Bangalore"
# obj.new3()



class employee():
    name=" "
    def fun1(self):
        print(self.name)

class department(employee):
    location=" "
    def fun2(self):
        print(self.location)

class admin(department):
    def fun3(self):
        print(" name: ",self.name)
        print(" location: ",self.location)

obj=admin()
obj.name="vishu"
obj.location="Bangalore"
obj.fun2()






