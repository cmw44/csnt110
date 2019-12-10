"""
inclass10.py - Cameron Wertelka
Import BeautifulSoup from the bs4 module
Make function makeStrPair an assign key and value
    Write '            "' + key + '" : "' + value + '"' and store as temp
    Return temp
make function makeListPair and assign key and value
    Write '            "' + key + '" : [' + value + ']' and store as temp
    Return temp
Open "inclass10.xml" for reading, store handle as infile
Read entire contents from infile, store as contents
Call BeautifulSoup(contents,'xml'), store as soup
Call soup.find_all('student') to get a list of <student> elements store as student_list
Open "inclass10.json" for writing, store as outfile
Write '{\n  "records" : {\n' to outfile
Write '      "students" : [\n' to outfile
For i in range of 0 to the length of student_list:
    Make student_list an index, save as student
    Get text by finding 'name' in file, store as name
    Get text by finding 'scores' in file, store as scores
    Get text by finding 'major' in file, store as major
    Write '         {\n' to outfile
    Write makeStrPair('name',name) + ",\n" to outfile
    Write makeStrPair('major',major) + ",\n" to outfile
    Write makeListPair('scores',scores) + "\n" to outfile
    Write '         }' to outfile
    If i is lesser than the length of student_list
"""
from bs4 import BeautifulSoup

def makeStrPair(key, value):
    temp = '            "' + key + '" : "' + value + '"'
    return temp


def makeListPair(key, value):
    temp = '            "' + key + '" : [' + value + ']'
    return temp

infile = open("inclass10.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')
student_list = soup.find_all('student')
outfile = open("inclass10.json","w")
outfile.write('{\n  "records" : {\n')
outfile.write('      "students" : [\n')
for i in range(0,len(student_list)):
    student = student_list[i]
    name = student.find('name').get_text()
    scores = student.find('scores').get_text()
    major = student.find('major').get_text()
    outfile.write('         {\n')
    outfile.write(makeStrPair('name',name) + ",\n");
    outfile.write(makeStrPair('major',major) + ",\n");
    outfile.write(makeListPair('scores',scores) + "\n");
    outfile.write('         }')
    if (i < len(student_list) - 1):
        outfile.write(',');
    outfile.write('\n')
outfile.write('      ],\n')
outfile.write('      "course" : {\n')
titles = soup.find('titles').get_text()
weights = soup.find('weights').get_text()
outfile.write(makeListPair('titles',titles) + "\n");
outfile.write(makeListPair('weights',weights) + "\n");
outfile.write('      }\n')
outfile.write('   }\n}')
outfile.close()
