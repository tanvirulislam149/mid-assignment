class Library:
    book_list = []
    def __init__(self, library_name):
        self.library_name = library_name
    def entry_book(self, book_id, title, author, availability):
        book = Book(book_id, title, author, availability)
        self.book_list.append(book)



class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def __repr__(self):
        return 

batighor = Library("batighor")
batighor.entry_book(3, "Database book", "Jhankar Mahbub", True)
batighor.entry_book(4, "DS", "Sumit Saha", True)
batighor.entry_book(5, "Algorithm", "Rahat Khan", True)

pciu_lib = Library("pciu_lib")
pciu_lib.entry_book(10, "SPL", "Morshed sir", True)
pciu_lib.entry_book(10, "Physics", "Abadat sir", True)

for book in batighor.book_list:
    print(book.title)