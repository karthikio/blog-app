from src.settings import LOGIN_URL
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, FormView, View
from django.contrib.auth import logout
from django.conf import settings
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
  

class LogoutView(View):
  def get(self, request):
    logout(request)
    return redirect(settings.LOGIN_URL)