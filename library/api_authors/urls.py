from django.urls import path

from api_authors.views import AuthorsView

urlpatterns = [
    path('', AuthorsView.as_view())
]
