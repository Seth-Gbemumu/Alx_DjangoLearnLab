from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path ("books/", list_books, name ="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]


