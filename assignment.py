class Library:
    book_list = []
    def __init__(self, library_name):
        self.library_name = library_name
    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.__availability = availability

    def get_book_id(self):
        return self.__book_id

    def get_availability(self):
        return self.__availability
    
    def set_availability(self, data):
        self.__availability = data 

    @staticmethod
    def borrow_book(book_id):
        flag = False
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                if book.get_availability() == True:
                    book.set_availability(False)
                    print(f"Here is your {book.title} book")
                else:
                    print("This book is already borrowed")
                flag = True
                break
        if flag == False:
            print("Book not found")

    @staticmethod
    def return_book(book_id):
        flag = False
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                if book.get_availability() == False:
                    book.set_availability(True)
                    print(f"Thanks for returning the {book.title} book")
                else:
                    print("Wrong book id")
                flag = True
                break
        if flag == False:
            print("Book not found")

    @staticmethod
    def view_book_info(id):
        flag = False
        for book in Library.book_list:
            if book.get_book_id() == id:
                print(f"Id: {book.get_book_id()}, Title: {book.title}, Author: {book.author}, Availability: {book.get_availability()}")
                flag = True
                break
        if flag == False:
            print("Book not found")

# Making book instances
ds = Book(3, "Data Structure", "Jhankar", True)
algo = Book(4, "Algorithm", "Mahbub", True)
db = Book(5, "Database", "Rahat", True)

# entering books in a specific library
batighor = Library("batighor")
batighor.entry_book(ds)
batighor.entry_book(algo)
batighor.entry_book(db)

# Printing books
for book in Library.book_list:
    print(f"Id: {book.get_book_id()}, Title: {book.title}, Author: {book.author}, Availability: {book.get_availability()}")

# Manual functions
Book.borrow_book(4)
Book.borrow_book(4)
# Book.return_book(4)
Book.return_book(2)
Book.view_book_info(4)

for book in Library.book_list:
    print(f"Id: {book.get_book_id()}, Title: {book.title}, Author: {book.author}, Availability: {book.get_availability()}")


# Menu system implementation
print("-----Options-----------")
print("""1 -> View all book
2 -> Borrow book
3 -> Return book
4 -> Exit
""")
while True:
    n = int(input("Enter option: "))
    if n == 1:
        for book in Library.book_list:
            print(f"Id: {book.get_book_id()}, Title: {book.title}, Author: {book.author}, Availability: {book.get_availability()}")
    elif n == 2:
        id = int(input("Enter book id: "))
        Book.borrow_book(id)
    elif n == 3:
        id = int(input("Enter book id: "))
        Book.return_book(id)
    elif n == 4:
        print("Closing the system.")
        break
