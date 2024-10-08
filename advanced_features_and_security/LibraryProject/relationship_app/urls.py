from django.urls import path
from . import views
#from .views import list_books, LibraryDetailView, Register
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book



urlpatterns = [
    path ("books/", views.list_books, name ="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/edit', edit_book, name="edit_book"),
    path('delete_book/<int:pk>/delete', delete_book, name='delete_book')
]


