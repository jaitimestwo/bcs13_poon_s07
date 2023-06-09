class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_publication_year(self):
        return self.publication_year
    def is_book_available(self):
        return self.is_available
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

library = []

# functions
def display_available_books():
    print("________________")
    print("Available Books:")
    for index, book in enumerate(library):
        if book.is_book_available():
            print(f"{index}: {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")
def add_book_to_library():
    title = input("Enter title: ")
    author = input("Enter author: ")
    publication_year = input("Enter publication year: ")
    book = Book(title, author, publication_year)
    library.append(book)
def borrow_book():
    display_available_books()
    borrow_index = int(input("Enter book index to borrow: "))
    if borrow_index < 0 or borrow_index >= len(library):
        display_error_message()
    else:
        book = library[borrow_index]
        if book.borrow_book():
            print(f"'{book.get_title()}' borrowed.")
            display_available_books()
        else:
            print(f"'{book.get_title()}' is currently unavailable.")
            display_available_books()
def return_book():
    display_available_books()
    return_index = int(input("Enter book index to return: "))
    if return_index < 0 or return_index >= len(library):
        display_error_message()
    else:
        book = library[return_index]
        if book.return_book():
            print(f"'{book.get_title()}' returned.")
            display_available_books()
        else:
            print(f"'{book.get_title()}' is already in the library.")
            display_available_books()
def display_error_message():
    print("Error!")

# input
while True:
    try:
        selector = input("Would you like to add a book? Y/N: ")
        if selector == "Y" or selector == "y":
            add_book_to_library()
        elif selector =="N" or selector == "n":
            display_available_books()
            break
        else:
            print("Invalid input!")
    except:
        continue

selection_menu = {
    1: borrow_book, 2: return_book, 3: exit
}

while True:
    print("________________")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Exit")
    sel = int(input("Enter your choice (1-3): "))
    if sel in selection_menu:
        selection_menu[sel]()
    else:
        print("Error!")