from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from .bl.bl import increase_visitors
from .forms import LoginUserForm, RegisterUserForm
from .models import Book


from django.contrib.auth import logout, login
from django.shortcuts import redirect

from .tasks import increase_visitors_shared


def api_books(request):
    books = Book.objects.all(

    ).select_related(
        'publisher',
    ).prefetch_related(
        'authors',
    ).only(
        'title', 'price', 'publisher'
    ).order_by('-id')

    result = [
        {
            'title': book.title,
            'pages': book.pages,
            'price': float(book.price)
        }
        for book in books
    ]
    data = {'result': result, 'count': len(result)}

    return JsonResponse(data)





class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class BookListView(ListView):
    queryset = Book.objects.all(
    ).select_related(
        'publisher',
    ).prefetch_related(
        'authors',
    ).only(
        'title', 'price', 'publisher'
    ).order_by('-id')

    template_name = 'books/book_list.html'
    paginate_by = 2



def book_list(request):
    limit = int((request.GET.get('limit') or 10))
    skip = int((request.GET.get('skip') or 0))

    increase_visitors_shared.delay()

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
    ).order_by('-id')[skip:skip+limit]  # LIMIT 20 OFFSET 10

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

    context = {
        'book': book,
        'age': 555
    }
    return render(request, 'books/book_detail.html', context)


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_add.html'
    success_url = '/'
    fields = '__all__'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_add.html'
    success_url = '/'
    fields = '__all__'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = '/'
