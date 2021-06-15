from django.db import models
from django.db.models.base import Model
from account.models import User


def upload_path(instance, filename):
    return  'images/{0}/profile/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic = models.ImageField(default='default.png', upload_to=upload_path)
  name = models.CharField(max_length=255)
  bio = models.TextField(max_length=500)
  privacy = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username