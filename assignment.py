class Library:
    book_list = []
    def __init__(self, library_name):
        self.library_name = library_name
    def entry_book(self, book):
        # book = Book(book_id, title, author, availability)
        self.book_list.append(book)



class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    @staticmethod
    def borrow_book(book_id):
        flag = False
        for book in Library.book_list:
            if book.book_id == book_id:
                if book.availability == True:
                    book.availability = False
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
            if book.book_id == book_id:
                if book.availability == False:
                    book.availability = True
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
            if book.book_id == id:
                print(f"Id: {book.book_id}, Title: {book.title}, Author: {book.author},Availability: {book.availability}")
                flag = True
                break
        if flag == False:
            print("Book not found")


ds = Book(3, "Data Structure", "Jhankar", True)
algo = Book(4, "Algorithm", "Mahbub", True)
db = Book(5, "Database", "Rahat", True)
batighor = Library("batighor")
batighor.entry_book(ds)
batighor.entry_book(algo)
batighor.entry_book(db)

for book in Library.book_list:
    print(f"Id: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}")

Book.borrow_book(4)
Book.borrow_book(4)
Book.return_book(4)
Book.return_book(2)
Book.view_book_info(4)

for book in Library.book_list:
    print(f"Id: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}")

while True:
    n = int(input("Enter option: "))
    if n == 1:
        for book in Library.book_list:
            print(f"Id: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}")
    elif n == 2:
        id = int(input("Enter book id: "))
        Book.borrow_book(id)
    elif n == 3:
        id = int(input("Enter book id: "))
        Book.return_book(id)
    elif n == 4:
        print("Closing the system.")
        break

