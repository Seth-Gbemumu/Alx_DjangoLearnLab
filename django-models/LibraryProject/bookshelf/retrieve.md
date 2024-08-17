from bookshelf.moodels import Book
retrieve_book = Book.objects.get(title="1984")
print(retrieve_book)

# Output: 1984 by George Orwell (1949)
