from django.urls import path
from .views import (
    BookListView,
    book_list,
    book_detail,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    logout_user,
    LoginUser,
    RegisterUser,
    api_books,
)

urlpatterns = [
    path('class-view/', BookListView.as_view()),
    path('', book_list, name='index'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/add/', BookCreateView.as_view(), name='book_add'),
    path('book/edit/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),

    path('logout', logout_user, name='logout'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),

    path('api/v1/', api_books, name='api_books'),


]
