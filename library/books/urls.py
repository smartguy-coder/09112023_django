from django.urls import path
from .views import BookListView, book_list, book_detail

urlpatterns = [
    path('class-view/', BookListView.as_view()),
    path('', book_list),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]
