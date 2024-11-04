from django.shortcuts import redirect, render
from books.models import Book
from django.core.paginator import Paginator

from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book
from django.utils.dateparse import parse_date
from django.http import Http404

def books_view(request):
    books = Book.objects.all().order_by('pub_date')
    paginator = Paginator(books, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'books/books_list.html', {'books': page_obj, 'page': page_obj})

def books_by_date_view(request, pub_date):
    # Преобразуем строку в дату
    date = parse_date(pub_date)
    if not date:
        raise Http404("Invalid date format. Use YYYY-MM-DD.")

    # Получаем книги за выбранную дату
    books = Book.objects.filter(pub_date=date)
    if not books.exists():
        raise Http404("No books found for this date.")

    # Поиск предыдущей и следующей даты с книгами
    previous_date = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()

    context = {
        'books': books,
        'pub_date': pub_date,
        'previous_date': previous_date.pub_date if previous_date else None,
        'next_date': next_date.pub_date if next_date else None,
    }
    return render(request, 'books/books_by_date.html', context)



def index(request):
    return redirect('books')