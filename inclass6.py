"""
inclass6.py - Cameron Wertelka
Ask user to enter filename of file to process,
   store as filename
Open filename for reading, store handle as infile
Read all lines from infile, store as list called lines
Close infile
With filename, Replace ".csv" with ".xml", 
   store as outfilename 
Open outfilename for writing, store handle as outfile 
Write xml declaration header to outfile
Write '<data>\n' to outfile
For each line in lines
   Write '  <subject>\n' to outfile
        Write '        <name>' + tokens[0] + '</name>\n' to outfile
        Write '        <sex>' + tokens[1] + '</sex>\n' to outfile
        Write '        <height>' + tokens[2] + '</height>\n' to outfile
        Write '        <weight>' + tokens[3] + '</weight>\n' to outfile
   Write '  </subject>\n' to outfile
Write '</data>' to outfile
Close outfile
"""
filename = input("Enter name of file to process: ")
infile = open(filename,"r")
lines = infile.readlines()
infile.close()
outfilename = filename.replace(".csv",".xml")
outfile = open(outfilename,"w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<data>\n')
print("lines:",lines)
for line in lines:
    tokens = line.strip().split(",")
    outfile.write ("   <subject>\n")
    outfile.write ('        <name>' + tokens[0] + '</name>\n')
    outfile.write ('        <sex>' + tokens[1] + '</sex>\n')
    outfile.write ('        <height>' + tokens[2] + '</height>\n')
    outfile.write ('        <weight>' + tokens[3] + '</weight>\n')
    outfile.write ("   </subject>\n")
outfile.write('</data>')
outfile.close()
