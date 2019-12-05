"""
hw8.py - Cameron Wertelka
Import json module

Define function fixName(nameString)
    Split nameString on ",", store as tokens
    Strip tokens[1] + " " + Strip tokens[0], store as name
    Return name
    
Define function makeAverage(numlist)
    Set total = 0 
    for each num in numlist
        total = total + num
    Divide total by length of numlist, store as average
    Format average to 2 decimal places
    Return average
    
Ask user to enter name of file to process, store as filename
Open filename for reading, store handle as infile
Read entire contents of infile, store as contents
Call json.loads(contents), store result as students_d
Store students_d["roster"] as student_list

"""
import json

def fixName(nameString):
    tokens = nameString.split(',')
    name = tokens[1].strip() + " " + tokens[0].strip()
    return name 

def makeAverage(numlist):
    return '90.00'
    
#filename = input("Enter name of JSON file to process: ")
filename = "hw8.json"
infile = open(filename,'r')
contents = infile.read()
students_d = json.loads(contents)
student_list = students_d["roster"]
for student in student_list:
    namestring = student["name"]
    numlist = student["hwscores"]
    name = fixName(namestring)
    average = makeAverage(numlist)
    print(name + "'s hw average:",average)
