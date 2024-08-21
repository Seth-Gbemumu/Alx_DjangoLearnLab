from django.shortcuts import render
#from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"list_books": books}
    return render (request, "relationship_app/list_books.html", context)


class LibraryDetail(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('login')

class register(CreateView):
    form_class = UserCreationForm()
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy('login')

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')