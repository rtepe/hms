from django.shortcuts import render
from .models import Book

def home_view(request):
    # Create a new book
    new_book = Book(
        title="Django with MongoDB",
        author="John Doe",
        published_date="2024-12-01"
    )
    new_book.save()

    # Fetch all books
    books = Book.objects()

    return render(request, 'home.html', {'books': books})
