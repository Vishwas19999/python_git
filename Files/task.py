#csv
import csv

class Image:

    def ImageDetails(self):
        with open('tas1.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))


class Imagefile(Image):

    def ImagefileDetails(self):
        super()

        with open('tas1.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))

obj = Imagefile()
print("-----Image Detail-----")
obj.ImageDetails()

print("-----Imagefile Detail-----")
obj.ImagefileDetails()





 #json
import json

class Image:

    def ImageDetails(self):
        with open('newtask.json') as jsonfile:
            data = json.load(jsonfile)
            for row in data:
                print(data)


class Imagefile(Image):

    def ImagefileDetails(self):
        super()

        with open('newtask1.json') as csvfile:
            data = json.load(csvfile)
            for row in data:
                print(data)

obj = Imagefile()
print("-----Image Detail-----")
obj.ImageDetails()

print("-----Imagefile Detail-----")
obj.ImagefileDetails()





# xml
from bs4 import BeautifulSoup
with open('task1.xml', 'r') as f:
   data = f.read()
   print(data)

