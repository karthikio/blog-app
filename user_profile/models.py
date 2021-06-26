from django.db import models
from account.models import User
from django.urls import reverse


def upload_path(instance, filename):
    return  'images/{0}/profile/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic = models.ImageField(default='default.jpg', upload_to=upload_path)
  name = models.CharField(max_length=255, null=True, blank=True)
  bio = models.TextField(default='Hey, I\'m using blog app', max_length=500, blank=True, null=True)
  privacy = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username

  def get_absolute_url(self):
    return reverse('profile-detail-view', kwargs={'username': self.user.username})