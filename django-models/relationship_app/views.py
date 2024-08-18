from django.shortcuts import render
#from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {"book_list": books}
    return render (request, "relationship_app/book_list.html", context)


class LibraryDetail(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_name = "library"




    



    
