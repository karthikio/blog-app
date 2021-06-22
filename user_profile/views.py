from django.shortcuts import render
from .models import Profile
from django.views.generic import UpdateView
from account.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# class ProfileDetailView(DetailView):
#   model = Profile

@login_required
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



class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
  model = Profile
  fields = ('name', 'profile_pic', 'bio', 'privacy',)
  template_name = 'user_profile/update_profile.html'
  success_url = reverse_lazy('posts-list-view')

  def test_func(self):
    profile = self.get_object()
    if self.request.user == profile.user:
      return True
    return False
