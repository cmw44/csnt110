from bs4 import BeautifulSoup
infilename = input("Enter name of xml file to modify: ")
#infilename = "students.xml"
outfilename = infilename.replace('.xml','_extra.xml')
contents = open(infilename).read()
soup = BeautifulSoup(contents,'xml')
students = soup.find_all('student')
outfile = open(outfilename,"w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<?xml-stylesheet rel="stylesheet" href="proj1.css" ?>\n')
outfile.write('<students>\n')
header = '''  <student>
    <name id="header">Name</name>
    <major id="header">Major</major>
    <status id="header">Status</status>
    <credits id="header">Credits</credits>
  </student>'''
outfile.write(header + "\n")
cr = soup.new_tag('credits')
cr.string = " - "
for student in students:
    if (student.find('credits') != None):
       outfile.write(str(student))
    else:
        student.append(cr)
        outfile.write(str(student))
outfile.write('</students>')
outfile.close()
