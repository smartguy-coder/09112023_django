from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'
