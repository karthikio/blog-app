from django.db import models
from django.shortcuts import render
from .models import Profile
from django.views.generic import DetailView
from account.models import User
from django.http import HttpResponse

# class ProfileDetailView(DetailView):
#   model = Profile

def ProfileDetailView(request, username):
  try:
    user = User.objects.get(username=username)
    obj = Profile.objects.get(user=user)
  except:
    return HttpResponse('none')
  
  context = {
    "object": obj,
  }
  return render(request, 'user_profile/profile_detail.html', context)