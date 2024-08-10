# Delete the Book Instance

### Command:

from bookshelf.models import Book

retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()

try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book deleted successfully.")
