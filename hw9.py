"""
hw9.py - Cameron Wertelka
Import json module
Open "cars.json" for reading, stoer as infile
read all of infile contents, store as contents
Call json.loads(contents), store result as cars_d
Store cars_d["cars"] as cars_list

"""
import json

def makeElement(tagName, value):
    temp = '      <' + tagName + '>' + str(value)
    temp += '</' + tagName + '>\n'
    return temp

def makeCar(car):
    temp = '   <car>\n'
    temp += makeElement('make',car["make"])
    temp += makeElement('model',car["model"])
    temp += makeElement('price',car["price"])
    temp += '   </car>\n'
    return temp

infile = open("cars.json","r")
contents = infile.read()
cars_d = json.loads(contents)
cars_list = cars_d["cars"]
for car in cars_list:
    print(makeCar(car))
    
