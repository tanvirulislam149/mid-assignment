class Library:
    book_list = []
    def __init__(self, library_name):
        self.library_name = library_name
    def entry_book(self, book):
        # book = Book(book_id, title, author, availability)
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.__availability = availability

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

algo.title = "Lasdf"
print(algo.title)