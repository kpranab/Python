from django.http import Http404
from django.shortcuts import render

from .models import Book


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exists.')
    return render(request, 'books/detail.html', {'book': book})
