"""
inclass10.py - Cameron Wertelka
Import BeautifulSoup from the bs4 module
Open "inclass10.xml" for reading, store handle as infile
Read entire contents from infile, store as contents
Call BeautifulSoup(contents,'xml'), store as soup
Call soup.find_all('student') to get a list of <student> elements
    store as student_list
"""
from bs4 import BeautifulSoup

def makeStrPair(key, value):
    temp = '            "' + key + '" : "' + value + '"'
    return temp


def makeListPair(key, value):
    temp
infile = open("inclass10.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')
student_list = soup.find_all('student')
outfile = open("inclass10.json","w")
outfile.write('{\n  "records" : {\n')
outfile.write('      "students" : [\n')
for student in student_list:
    name = student.find('name').get_text()
    outfile.write('            {\n')
    outfile.write(makeStrPair('name',name) + ",\n");
    outfile.write('            }
    print(makeStrPair('name',name))
outfile.write('      ]\n')
outfile.write('   }\n}')
outfile.close()
