from django import forms
from django.views.generic.detail import DetailView
from .models import Post

class PostForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title'}))
  class Meta:
    model = Post
    fields = "__all__"



    


