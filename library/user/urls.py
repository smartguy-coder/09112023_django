from django.urls import path

from user.views import RegisterView, RetrieveUserView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view())
]
