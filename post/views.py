import django
from django.forms.forms import Form
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView, LoginRequiredMixin):
  login_url = '/login/'
  redirect_field_name = 'login'
  model = Post
  paginate_by = 10


class PostDetailView(DetailView):
  model = Post
  slug_field = "id"


class PostFormView(CreateView):
  model = Post
  fields = ('title', 'image', 'body',)
  template_name = 'post/post_create.html'
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def form_invalid(self, form):
    return super().form_invalid(form)




