class Library:
    book_list = []
    def __init__(self):
        pass
    def entry_book(self, book_id, title, author, availability):
        book = Book(book_id, title, author, availability)
        self.book_list.append(book)



class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    
