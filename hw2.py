"""
hw2.py Cameron Wertelka
This program will write to hw2.html by using:
python3 hw2.py > hw2.html
"""
name = input("Enter your name: ")
major = input("Enter your major: ")
last = input("Enter last programming course taken: ")

out = """<html>
    <head>
        <link rel="stylesheet" type="text/css" href="hw2.css">
    </head>
    <body>"""
print(out)
print('     <p class="name">' + name + '</p>')
print('     <p class="major">' + major + '</p>')
print('     <p class="last">' + last + '</p>')

outtwo = """    </body>
</html>"""
print(outtwo)

