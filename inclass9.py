"""
inclass9.py - Cameron Wertelka
Import json module

Define function makeAverage(num_list)
    Set total = 0
    For each num in num_list
        total = total + num
    Divide total by length of num_list, store as average
    Format average to show 2 digits after the decimal place
    Return average
    
Ask user to enter name of file to process, store as infilename
Open infilename for reading, store handle as infile
Rad all of infil, store as contents
Call json.loads(content), store result as students_d
"""
import json

def makeAverage(num_list):
    total = 0
    for num in num_list:
        total = total + num
    average = total/len(num_list)
    average = '{:.2f}'.format(average)
    return average
infilename = input("Enter name of JSON file to process: ")
infile = open(infilename,"r")
contents = infile.read()
students_d = json.loads(contents)
students_list = students_d["students"]
for student in students_list:
    print(student["name"] + ", hw average:",makeAverage(student["hwscores"]) + ", exam average: " + makeAverage(student["exams"]))
