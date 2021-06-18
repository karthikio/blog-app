from django.forms.forms import Form
from django.shortcuts import render
from django.views.generic import DeleteView, FormView
from .forms import RegisterForm, LoginForm
from .models import User



class UserDeleteView(DeleteView):
  pass


class RegisterView(FormView):
  form_class = RegisterForm
  model = User


class LoginView(FormView):
  form_class = LoginForm
  template_name = 'account/login.html'

