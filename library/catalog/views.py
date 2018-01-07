from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Issues,Students
from django.views import generic

def index(request):
    num_books=Books.objects.count()
    # Available books (status = 'a')
    num_books_available=Books.objects.filter(available__exact='a').count()
    

    return render(request,'index.html',context={'num_books':num_books,'num_books_available':num_books_available})

class BookList(generic.ListView):
 model = Books
 context_object_name = 'Book Shelf'
 queryset = Books.objects.filter(title__icontains='Game')[:5]
