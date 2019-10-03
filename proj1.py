"""
proj1.py by Cameron Wertelka
Ask user to enter filename to save file, store as filename
Open filename for writing, store handle as outfile
Write '<?xml version="1.0" ?>\n' to outfile
Write '<students>\n' to outfile
Set done to false
While not done
    Ask to enter a student (y/n), store as response 
    Strip response, force response to lowercase
    If reponse is 'n'
    Set done to True
Write '</students>' to outfile
Close outfile
"""

#filename = input("Enter name of XML file to write to: ")
filename = "students.xml"
outfile = open(filename, "w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<students>\n')
done = False
while (not done):
    response = input("Enter a student? (y/n): ")
    response = response.strip().lower()
    if (response == 'n'):
        done = True
    elif (response == 'y'):
        name = input("Enter student's name: ")
        name = name.strip().title()
        major = input("Enter student's major: ")
        major = major.strip().upper()
        status = input("Is student full-time? (y/n)? ")
        status = status.strip().lower()
        if (status == 'n'):
            credits = input("Enter number of credits for part-time: ")
        elif (status == 'y'):
        outfile.write(' <student>\n')
        outfile.write('     <name>' + name + '</name>\n')
        outfile.write('     <major>' + major + '</major>\n')
        outfile.write('     <status>' + status + '</status>\n')
        outfile.write('     <credits>' + credits + '</credits>\n')
        outfile.write(' </student>\n')
outfile.write('</students>')
outfile.close()
