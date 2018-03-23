'''
Gautam Mehta
CIS 41A Fall 2017
Unit J take-home assignment
''' 
class LibraryPatron:
    def __init__(self, name):
        self.name= name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) >= checkOutLimit:
            print ("Sorry", self.name, "you are at your limit of", checkOutLimit, "books")
        else:
            self.booksCheckedOut.append(bookTitle)
            print (self.name, "has checked out", bookTitle)
            
    def returnBook(self, book): 
        self.booksCheckedOut.remove(book[0])
        print (self.name, "has returned", book[0])
        
    def printCheckedOutBooks(self):
        print (self.name, "has the following books checked out: ")
        for i in self.booksCheckedOut:
            print (i)
            
class AdultPatron(LibraryPatron):
    def __init__(self,name):
        name= LibraryPatron.__init__(self,name)
        self.checkOutLimit= 4
        
    def checkOutBook(self,book):
        LibraryPatron.checkOutBook(self, self.checkOutLimit, book[0])
        
class JuvenilePatron(LibraryPatron):
    def __init__(self,name):
        name= LibraryPatron.__init__(self,name)
        self.checkOutLimit= 2
        
    def checkOutBook(self,book):
        if book[1] != "Juvenile":
            print ("Sorry", self.name, book[0], "is an adult book")
        else:
            LibraryPatron.checkOutBook(self, self.checkOutLimit, book[0])
        


book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()

"""
Execution Results:
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out: 
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out: 
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out: 
The Da Vinci Code
The Hobbit
"""