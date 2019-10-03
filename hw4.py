"""
hw4.py by Cameron Wertelka
Ask user to enter name of file to write to, store as filename
Open filename for writing, store handle as outfile
set programRunning to True
While programRunning is True,
set variable food to gather input from users
strip variable food to title case
if input is 'done'
set programRunning to false
otherwise set a second variable called food_type to gather input from users
strip food_type
Write '  <item>\n' to outfile
Write '     <name>\n' to outfile
Write food to outfile
Write '     </name>\n' to outfile
Write '     <type>\n' to outfile
Write food_type to outfile
Write '     </type>\n' to outfile
Write '  </item>\n' to outfile
Write '</menu>' to outfile
CLose outfile
"""

#filename = input("Enter name of XML file to write to: ")
filename = "menu.xml"
outfile = open(filename, "w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<menu>\n')

programRunning = True
while (programRunning):
    food = input("Enter a food item or 'done' if finished: ")
    food = food.strip().title()
    if (food == "Done"):
        programRunning = False
    else: 
        food_type = input("Enter the food item type: ")
        food_type = food_type.strip()
        outfile.write('  <item>\n')
        outfile.write('     <name>\n')
        outfile.write(food)
        outfile.write('     </name>\n')
        outfile.write('     <type>\n')
        outfile.write(food_type)
        outfile.write('     </type>\n')
        outfile.write('  </item>\n')
    
outfile.write('</menu>')
outfile.close
