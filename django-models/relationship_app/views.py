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

def Admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def Librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def Member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-Based Views
@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')