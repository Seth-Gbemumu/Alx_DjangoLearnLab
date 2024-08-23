from django.contrib import admin
from .models import UserProfile, Library, Librarian, Book, Author

# Register your models here.

admin.site.register(Book, Author, Librarian, Library, UserProfile)
