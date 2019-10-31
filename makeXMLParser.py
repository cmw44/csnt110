import xml.sax 
class MyHandler(xml.sax.ContentHandler): 
    """ class to perform xml parsing """ 
    def __init__(self): 
        xml.sax.ContentHandler.__init__(self)
        self.elementList = []
        self.depth = 0
        
    def startElement(self,name,attr):
        self.depth = self.depth + 1
        if ([name,self.depth] in self.elementList):
            pass
        else:
            self.elementList.append([name,self.depth])
            
    def endElement(self,name):
        self.depth = self.depth - 1
    
filename = input("Enter name of xml file to process: ")
parser = xml.sax.make_parser() 
handler = MyHandler() 
parser.setContentHandler(handler) 
parser.parse(filename)
filename = filename.replace(".xml","xml_parse.py")
outfile = open(filename,"w")
outfile.write('import xml.sax\n')
outfile.write('class CustomHandler(xml.sax.ContentHandler):\n')
outfile.write('    """ custom class to parse XML file """\n')
outfile.write('    def __init__(self):\n')
outfile.write('        xml.sax.ContentHandler.__init__(self)\n')
for element in handler.elementList:
    element[0] = element[0].replace('-','')
    outfile.write('        self.in' + element[0].capitalize() + ' = False\n')
outfile.write('\n')
outfile.write('    def startElement(self,name,attr):\n')
for i in range(0,len(handler.elementList)):
    element = handler.elementList[i]
    if (i == 0):
        outfile.write('        if')
    else:
        outfile.write('        elif')
    #element[0] = element[0].replace('-','')
    outfile.write(' (name == "' + element[0] + '"):\n')
    outfile.write('            ')
    outfile.write('self.in' + element[0].capitalize() + ' = True\n')
outfile.write('\n    def endElement(self,name):\n')
for i in range(0,len(handler.elementList)):
    element = handler.elementList[i]
    if (i == 0):
        outfile.write('        if')
    else:
        outfile.write('        elif')
    outfile.write(' (name == "' + element[0] + '"):\n')
    outfile.write('            ')
    outfile.write('self.in' + element[0].capitalize() + ' = False\n')
outfile.write('\n    def characters(self,data):\n')
levelcount = 0
lastlevel = 1
for i in range(0,len(handler.elementList)):
    element = handler.elementList[i][0]
    level = handler.elementList[i][1]
    if (level != lastlevel):
        levelcount = 0
    if (level == 1 and i == 0):
        outfile.write('        if')
        outfile.write(' (self.in' + element.capitalize() + '):\n')
    elif (level > 1):
        outfile.write(4*(level+1)*" ")
        if (levelcount == 0):
            outfile.write('if')
        else:
            outfile.write('elif')
        levelcount += 1
        outfile.write(' (self.in' + element.capitalize() + '):\n')
    lastlevel = level
outfile.write('\n')
footer = """filename = input("Enter name of xml file to process: ")
parser = xml.sax.make_parser()
handler = CustomHandler()
parser.setContentHandler(handler)
parser.parse(filename)"""
outfile.write(footer + '\n')
outfile.close()
