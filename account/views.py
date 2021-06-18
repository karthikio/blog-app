from django.shortcuts import render
from django.views.generic import DeleteView, FormView
from .forms import RegisterForm, LoginForm
from .models import User


class UserDeleteView(DeleteView):
  pass


class RegisterView(FormView):
  form_class = LoginForm
  model = User


class LoginView():
  pass
  