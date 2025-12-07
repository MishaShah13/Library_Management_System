# main.py

from library_module import Book, EBook, Library, DigitalLibrary, books_by_author, BookNotAvailableError

# Create a library
lib = Library()

# Add books
lib.add_book(Book("The Alchemist", "Paulo Coelho", "1"))
lib.add_book(Book("1984", "George Orwell", "2"))
lib.add_book(Book("Animal Farm", "George Orwell", "3"))

# Display all books
print("All Books:")
for b in lib.books:
    print(b.title)

# Books by specific author
print("\nBooks by George Orwell:")
for b in books_by_author(lib.books, "George Orwell"):
    print(b.title)

# Lend a book
try:
    lib.lend_book("2")
except BookNotAvailableError as e:
    print(e)

# Available books
print("\nAvailable Books:")
for b in lib:
    print(b.title)

# Digital library
dlib = DigitalLibrary()
dlib.add_ebook(EBook("Python Crash Course", "Eric Matthes", "4", "5MB"))

print("\nDigital Library Books:")
for b in dlib.books:
    print(b.title)
