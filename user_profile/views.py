from django.shortcuts import render
from .models import Profile
from django.views.generic import DetailView



class ProfileDetailView(DetailView):
  model = Profile
