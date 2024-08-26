from django.contrib import admin
from .models import UserProfile, Library, Librarian, Book, Author, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Book, Author, Librarian, Library, UserProfile)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
