"""
Cameron Wertelka - hw6.py
Ask user to enter input filename, store as filename
Open filename for reading, store handle as infile
Real all lines from infile, store as lines
Close infile
For each line in lines
    Strip line, split line on ",", store as tokens
"""

filename = input("Enter name of file to process: ")
infile = open(filename, "r")
lines = infile.readlines()
infile.close()
for line in lines:
    tokens = line.strip().split(",")
    total = 0
    for i in range(1, len(tokens)):
        total = total + float(tokens[i])
    average = total/len(tokens) - 1)
