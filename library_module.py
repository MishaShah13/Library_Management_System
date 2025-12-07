# library_module.py

# Book class
class Book:
    def __init__(self, title, author, isbn):
        # roman urdu: book ki basic maloomat
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_lent = False  # roman urdu: book lend hui ya nahi

# Custom exception
class BookNotAvailableError(Exception):
    # roman urdu: jab book available na ho
    pass

# Iterator for available books
class AvailableBooksIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # roman urdu: agla available book dhoondo
        while self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            if not book.is_lent:
                return book
        raise StopIteration

# Generator function for books by author
def books_by_author(books, author):
    # roman urdu: sirf specific author ki books return karo
    for book in books:
        if book.author.lower() == author.lower():
            yield book

# Library class
class Library:
    def __init__(self):
        # roman urdu: library ke andar books
        self.books = []

    def add_book(self, book):
        # roman urdu: nayi book add karo
        self.books.append(book)

    def remove_book(self, isbn):
        # roman urdu: ISBN se book remove karo
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def lend_book(self, isbn):
        # roman urdu: book lend karo, agar available nahi to error raise karo
        for book in self.books:
            if book.isbn == isbn:
                if book.is_lent:
                    raise BookNotAvailableError("Book pehle se lend ho chuki hai")
                book.is_lent = True
                return book
        raise BookNotAvailableError("Book available nahi hai")

    def return_book(self, isbn):
        # roman urdu: book return karo
        for book in self.books:
            if book.isbn == isbn:
                book.is_lent = False
                return True
        return False

    def __iter__(self):
        # roman urdu: iterator return karo
        return AvailableBooksIterator(self.books)

# DigitalLibrary inherits from Library
class DigitalLibrary(Library):
    def add_ebook(self, ebook):
        # roman urdu: ebook add karo
        self.add_book(ebook)

# EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, isbn, download_size):
        super().__init__(title, author, isbn)
        # roman urdu: ebook ka size
        self.download_size = download_size
