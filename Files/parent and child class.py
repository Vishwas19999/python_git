import json
class Employee:
    def employeeDetails(self):
        with open('newdata.json') as file:

           # for row in data:
              #  print(', '.join(row))

class Department(Employee):

    def departmentDetails(self):


        with open('department.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))



