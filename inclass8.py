"""
inclass8.py - Cameron Wertelka
Import json module

define function makeElement(name,val)
    Concatenate '      <' + name + '>' + str(val) + '</' + name + '>\n'
        store as temp
    return temp
    
Define function makeStudent(student):
    write '   <student>\n', save as temp
    write makeElement('name',student["name"]), add to temp
    write makeElement('major',student["major"]), add to temp
    write makeElement('credits',student["credits"]), add to temp
    write '   </student>\n', add to temp
    return temp

Open "students.json" for reading, store handle as infile
Read entire contents of infile, store as contents
Call json.loads(contents), store result as students_d
call students from students_d, save as students_list
Open students.xml for outfile to write to
write '<?xml version="1.0" ?>\n' to outfile
write '<students>\n' to outfile
For student in the students_list:
    write makeStudent(student) to outfile
Write '</students>' to outfile
Close outfile

--- Questions ---

"""
import json

def makeElement(name,val):
    temp = '      <' + name + '>' + str(val) + '</' + name + '>\n'
    return temp

def makeStudent(student):
    temp = '   <student>\n'
    temp += makeElement('name',student["name"])
    temp += makeElement('major',student["major"])
    temp += makeElement('credits',student["credits"])
    temp += '   </student>\n'
    return temp

infile = open("students.json", "r")
contents = infile.read()
students_d = json.loads(contents)
#print(students_d)
students_list = students_d["students"]
outfile = open("students.xml","w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<students>\n')
for student in students_list:
    outfile.write(makeStudent(student))
outfile.write('</students>')
outfile.close()
