from django.urls import path
from . import views
#from .views import list_books, LibraryDetailView, Register
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path ("books/", views.list_books, name ="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.Register.as_view, name='register'),
]


