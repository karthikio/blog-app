from django.shortcuts import render
from django.views.generic import (
  ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from user_profile.models import Profile
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(LoginRequiredMixin, ListView):
  model = Post
  paginate_by = 10

  def get_queryset(self):
    # filter with private account users
    private_users = Profile.objects.filter(privacy=True)
    if private_users:
      for i in private_users:
          qs = Post.objects.exclude(author=i.user).order_by('-id')
    else:
      qs = Post.objects.all().order_by('-id')
    return qs

  

class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
  model = Post
  fields = ('title', 'image', 'body',)
  template_name = 'post/post_create.html'
  success_message = 'New post created!'
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def form_invalid(self, form):
    return super().form_invalid(form)


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin,UserPassesTestMixin, UpdateView):
  model = Post
  fields = ('title', 'image', 'body',)
  template_name = 'post/post_update.html'
  success_message = "Post update success!"


  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False