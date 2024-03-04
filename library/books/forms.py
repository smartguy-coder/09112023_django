from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserFormMixin:
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))


class LoginUserForm(UserFormMixin, AuthenticationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'password'}))


class RegisterUserForm(UserFormMixin, UserCreationForm):
    email = forms.EmailField(label='email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
