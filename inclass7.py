"""
inclass7.py - 
We will use an index-based for loop to process main data

Ask user for the name of file to read. Save as infilename
Open aforementioned file
Read file lines, save as lines
Close the infile
Ask user for name of file to write output to
Open aforementioned file
Write '<?xml version="1.0" ?>\n' to outfile
Write '<students>\n' to outfile
Take lines[1], save as title_line
Take lines[-1], save as weights_line
Strip and split the weights_line by tab, or "\t". Save as weights
For i in range of lines 2 through length of lines, with the exception of line -1:
    Strip and split lines by tab, save as tokens
    Save totalWeight as 0
    Save totalWeightedScore as 0
    For j in range of lines 1 through the tokens:
        Float the tokens and strip the percentage symbol, save as score
        
"""
infilename = input("Enter file name to process: ")
infile = open(infilename,"r")
lines = infile.readlines()
infile.close()
outfilename = input("Enter file name to write output to: ")
outfile = open(outfilename,"w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<students>\n')
title_line = lines[1]
weights_line = lines[-1]
weights = weights_line.strip().split("\t")
for i in range(2, len(lines) -1):
   tokens = lines[i].strip().split("\t")
   totalWeight = 0
   totalWeightedScore = 0
   for j in range(1, len(tokens)):
      score = float(tokens[j].strip('%'))
      totalWeightedScore = totalWeightedScore + score*float(weights[j])
      totalWeight = totalWeight + float(weights[j])
   overallScore = totalWeightedScore/totalWeight
   overallScore = '{:.2f}'.format(overallScore)
   print("overallScore:",overallScore)
   names = tokens[0].split(",")
   outfile.write('   <student>\n')
   outfile.write('      <firstName>' + names[1].strip())
   outfile.write('</firstName>\n')
   outfile.write('      <lastName>' + names[0] + '</lastName>\n')
   outfile.write('      <overall>' + overallScore + '</overall>\n')
   outfile.write('   </student>\n')
outfile.write('</students>')
outfile.close()
