"""
inclass4.py by Cameron Wertelka
Ask user to enter name of file to write to, store as outfilename
Open outfilename for writing, store handle as outfile
Write '<?xml version="1.0" ?>\n' to outfile
Write '<animals>\n' to outfile
equate done to false
while done is false, set variable animal to it's input
strip variable animal
if user inputs "Done", set done = True
else write '<animal>' + animal + '</animal>\n' to outfile
write '</animals>' to outfile
close outfile
"""

#outfilename = input("Enter name of file to write to: ")
outfilename = "animals.xml" #hardcode to develop program
outfile = open(outfilename, "w")

outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<animals>\n')

done = False
while (not done):
    animal = input("Enter name of animal or 'done' if finished: ")
    animal = animal.strip().title()
    if (animal == "Done"):
        done = True
    else: 
        outfile.write('<animal>' + animal + '</animal>\n')
        
outfile.write('</animals>')
outfile.close()
