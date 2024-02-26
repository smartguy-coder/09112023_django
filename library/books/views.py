from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'


def book_list(request):
    # books = Book.objects.all()  # SELECT "books_book"."id", "books_book"."created_at", "books_book"."title",
                                  # "books_book"."price", "books_book"."last_changed_at",
                                  # "books_book"."pages", "books_book"."publisher_id"
                                  # FROM "books_book"


    books = Book.objects.all(   #  SELECT "books_book"."id", "books_book"."created_at", "books_book"."title",
                                # "books_book"."price", "books_book"."last_changed_at",
                                # "books_book"."pages", "books_book"."publisher_id",
                                # "books_publisher"."id",
                                # "books_publisher"."name" FROM "books_book" LEFT OUTER JOIN "books_publisher"
                                # ON ("books_book"."publisher_id" = "books_publisher"."id")
    ).select_related(
        'publisher',
    ).prefetch_related(
        'authors',
    ).only(
        'title', 'price', 'publisher'
    )[10:30]  # LIMIT 20 OFFSET 10

    #
    print(books.query)
    # print(books)
    # for book in books:
    #     print(book.__dict__)
    #     print(book.__dict__['pages'])
    #     print(book.pages)
    #     print(book.publisher.name)

    context = {
        'book_list': books,
        'age': 555
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, book_id):
    book = Book.objects.filter(
        id=book_id
    ).select_related(
        'publisher',
    ).prefetch_related(
        'authors',
    ).first()

    # print(book.query)


    context = {
        'book': book.__dict__,
        'age': 555
    }
    return render(request, 'books/book_detail.html', context)
