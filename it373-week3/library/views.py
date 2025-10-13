from django.shortcuts import render

from django.shortcuts import render
from .models import Book, Category

def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, "library/home.html", {"books": books, "categories": categories})

