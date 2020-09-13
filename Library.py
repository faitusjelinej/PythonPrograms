class Library_Program:

    def __init__(self,listofBooks):
        self.availableBooks = listofBooks


    def displayAvailablebooks(self):
        print()
        print("Available Books:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not Available in our list!")

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have now returned the book. Thank you!")

class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you would like to return: ")
        self.book = input()
        return self.book


library = Library_Program(['think big', 'battle field of the mind', 'wings of fire'])
customer = Customer()

while True:
    print("Enter 1 to display the Available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book" )
    print("Enter 4 to exit")

    userChoice = int(input())

    if userChoice is 1:
        library.displayAvailablebooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
