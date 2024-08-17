from relationship_app.models import Author, Book, Librarian, Library

#List books by all authors
author = Author.objects.get(name= "Author name")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {list(books_by_author)}")

#List books in a library
library = Library.objects.get(name= "Library name")
books_in_library = Book.objects.filter(library=library)
print(f"Books in {library.name}: {list(books_in_library)}")

#List librarians in libraries

librarian = Librarian.objects.get(library=library)
print(f"The librarian in {library.name} is {librarian.name}")