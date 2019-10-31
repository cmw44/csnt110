import xml.sax
class CustomHandler(xml.sax.ContentHandler):
    """ custom class to parse XML file """
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.inBooks = False
        self.inBook = False
        self.inTitle = False
        self.inAuthor = False
        self.inPrice = False

    def startElement(self,name,attr):
        if (name == "books"):
            self.inBooks = True
        elif (name == "book"):
            self.inBook = True
        elif (name == "title"):
            self.inTitle = True
        elif (name == "author"):
            self.inAuthor = True
        elif (name == "price"):
            self.inPrice = True

    def endElement(self,name):
        if (name == "books"):
            self.inBooks = False
        elif (name == "book"):
            self.inBook = False
        elif (name == "title"):
            self.inTitle = False
        elif (name == "author"):
            self.inAuthor = False
        elif (name == "price"):
            self.inPrice = False

    def characters(self,data):
        if (self.inBooks):
            if (self.inBook):
                if (self.inTitle):
                    print("Title:", data.strip(),end='')
                elif (self.inAuthor):
                    print(", Author:", data.strip())
                elif (self.inPrice):
                    pass

filename = input("Enter name of xml file to process: ")
parser = xml.sax.make_parser()
handler = CustomHandler()
parser.setContentHandler(handler)
parser.parse(filename)
