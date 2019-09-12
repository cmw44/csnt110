"""
inclass3.py Cameron Wertelka
Ask user to enter name, store as name
Ask user to enter major, store as major
Strip major, force major to uppercase
IF major is "CENT"
    Store "cent" as class_att
Else
    Store "other" as class_att
Print header
Print '     <h2 class="' + class_att + '">', end=''
Print name + "</h2>"
"""
name = input("Enter your name: ")
major = input("Enter your major: ")
major = major.strip().upper()
if (major == "CENT" or major == "CSNT"):
    class_att = "cent"
else: 
    class_att = "other"
print("""
<html>
    <head>
        <style>
            .cent {
            color: red;
            }
            .other {
            color: blue;
            }
        </style>
    </head>
    <body>""")
print('     <h2 class="' + class_att + '">', end='')
print(name + "</h2>")
print('     <p class="' + class_att + '">', end='')
print(major + "</p>")
print("""    </body>
</html>
""")
