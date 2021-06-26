from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def registerView(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}.')
      return redirect('login-view')
  else:
    form = RegisterForm()

  context = {
    'form': form,
  }

  return render(request, 'account/register.html', context)


def loginView(request, *args, **kwargs):
  user = request.user

  if user.is_authenticated:
    return redirect('posts-list-view')
  form = LoginForm()
  
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      user_name = User.objects.get(username=username)

      if user!= None:
        login(request, user)
        messages.success(request, f'You are now logged in as {user_name.username}!')
        return redirect('posts-list-view')
  else:
    form = LoginForm()
  
  context = {
    'form': form,
  }

  return render(request, 'account/login.html', context)


def logoutView(request):
  if not request.user.is_authenticated:
    return redirect('login-view')
  username = request.user
  logout(request)
  messages.success(request, f'You are now logged out {username}!')
  return redirect('login-view')


def contactView(request):
  return render(request, 'account/contact.html', {})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = User
  success_url = reverse_lazy('logout-view')

  def test_func(self):
    user = self.get_object()
    if self.request.user == user:
      return True
    return False

