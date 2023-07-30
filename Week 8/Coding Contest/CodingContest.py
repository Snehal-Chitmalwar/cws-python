class Book:

    def __init__(self):
        self.title = input("Enter the Title of the book:")
        self.author = input("Enter the Author of the boook:")
        self.num_copies = int(
            input("Enter the number of copies for this book available in the library:"))
        self.borrowers = list(input(
            "Enter the names of the borrowers for this book seperated by comma(,):").split(","))
        self.display_books()

    def display_books(self):
        print("\nBOOK DETAILS:\n")
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Number of Book copies: {self.num_copies}")
        print()

    def display_available_books(self):
        if self.num_copies > 0:
            print(f"Book Title: {self.title}")
            print(f"Book Author: {self.author}")
            print(f"Number of Book copies: {self.num_copies}")
            print()

    def display_borrowed_books(self):
        if len(self.borrowers) != 0:
            self.strBorrowserlist = ",".join(self.borrowers)
            print(f"Book Title: {self.title}")
            print(f"Book Author: {self.author}")
            print(f"Names of Borrowers: {self.strBorrowserlist}")
            print()

    def borrow_book(self, strNewBorrower):
        if self.num_copies >= 1:
            self.num_copies -= 1
            self.borrowers.append(strNewBorrower)
            print("You can borrow a book!")
            print(f"Remaining copies of book: {self.num_copies}")
            self.display_books()
            print(self.borrowers)
        else:
            print("Sorry!The book you want to borrow is not available in the Library.")

    def return_book(self, strNewBorrower):
        self.num_copies += 1
        self.borrowers.remove(strNewBorrower)
        print(f"Remaining copies of book: {self.num_copies}")
        self.display_books()
        print(self.borrowers)


book_library = []

while True:
    print("\n1) Add a Book in the Library")
    print("2) Search a Book in the Library")
    print("3) Display all the books in the Library")
    print("4) Display available books in the Library")
    print("5) Display borrowed books in the Library")
    print("6) Borrow a Book from the Library")
    print("7) Return a Book from the Library")
    print("8) Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        newBook = Book()
        book_library.append(newBook)
        print(f"A new Book is added to the Library: {book_library}")
    elif choice == 2:
        searchBook = input(
            "Enter Title of a book you want to search in the Library:")
        for i in book_library:
            if (i.title).lower() == searchBook.lower():
                i.display_books()
    elif choice == 3:
        if len(book_library) == 0:
            print("No books have been added yet in the Library")
        else:
            print("The list of books added in the Library:")
            for i in book_library:
                i.display_books()
    elif choice == 4:
        if len(book_library) == 0:
            print("No books have been added yet in the Library")
        else:
            print("The list of available books to borrow from the Library:")
            for i in book_library:
                i.display_available_books()
    elif choice == 5:
        if len(book_library) == 0:
            print("No books have been added yet in the Library")
        else:
            print("The list of borrowed books in the Library:")
            for i in book_library:
                i.display_borrowed_books()
    elif choice == 6:
        if len(book_library) == 0:
            print("No books have been added yet in the Library")
        else:
            book_to_borrow_title = input(
                "Enter the Book title you want to borrow from Library:")
            book_to_borrower_name = input("Enter your name:")
            for i in book_library:
                if (i.title).lower() == book_to_borrow_title.lower():
                    i.borrow_book(book_to_borrower_name)
    elif choice == 7:
        if len(book_library) == 0:
            print("No books have been added yet in the Library")
        else:
            book_to_borrow_title = input(
                "Enter the Book title you want to borrow from Library:")
            book_to_borrower_name = input("Enter your name:")
            for i in book_library:
                if (i.title).lower() == book_to_borrow_title.lower():
                    i.return_book(book_to_borrower_name)
    elif choice == 8:
        break
    else:
        print("Invalid Input")
