from relationship_app.models import Author, Book, Librarian, Library

#List books by all authors
author = Author.objects.get(name= "Author name")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {list(books_by_author)}")

#List books in a library
library_name = "library_name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library.name}: {list(books_in_library)}")

#List librarians in libraries

librarian = Librarian.objects.get(library=library)
print(f"The librarian in {library.name} is {librarian.name}")