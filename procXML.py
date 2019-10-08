from bs4 import BeautifulSoup
import bs4

def findLevel(myTag):
    count = 0
    done = False
    while (not done):
        if (myTag.parent == None):
            done = True
        else:
            myTag = myTag.parent
            count = count + 1
    return count

infilename = input("Enter name of XML file to process: ")
CSSfilename = infilename
if (CSSfilename.count("xml") > 0):
    CSSfilename = CSSfilename.replace("xml","css")
else:
    CSSfilename = CSSfilename + ".css"
contents = open(infilename).read()
soup = BeautifulSoup(contents,'xml')
root = soup.find(True)
#print root.name
descendants = root.descendants
element_names = [root.name]
for desc in descendants:
    if (type(desc) == bs4.element.Tag):
        name = desc.name
        if (name not in element_names):
            element_names.append(name)
CSSout = open(CSSfilename,"w")
for name in element_names:
    tag = soup.find(name)
    prompt = "Add style(s) for " + name + " ("
    prompt += str(findLevel(tag)) + ") (y/n)? "
    response = input(prompt)
    if (response.strip().lower() == 'y'):
        els = soup.find_all(name)
        for el in els:
            el['class'] = name
        CSSout.write(name + " {\n");
        done = False
        while (not done):
            style = input("Enter style or <enter> when done: ").strip()
            if (style == ""):
                done = True
            else:
                if (style.count(";") < 1):
                    style = style + ";"
                CSSout.write("  " + style + "\n")
        CSSout.write("}\n")
CSSout.close()
outfilename = infilename.replace(".xml","")
outfilename = outfilename + "_mod.xml"
outfile = open(outfilename,"w")
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<?xml-stylesheet rel="stylesheet" href="')
outfile.write(CSSfilename + '" ?>\n')
outfile.write(root.prettify())
outfile.close()
            
