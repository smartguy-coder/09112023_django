from django.urls import path
from .views import BookListView, book_list

urlpatterns = [
    path('', BookListView.as_view()),
    path('as-func', book_list),
]
