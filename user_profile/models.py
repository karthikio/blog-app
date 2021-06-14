from django.db import models
from django.db.models.base import Model
from account.models import User

def profile_upload_path(instance, filename):
    return 'uploads/profile_pic/images/%s/%s' % (instance.user.user.username, filename)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic = models.ImageField(upload_to=profile_upload_path)
  name = models.CharField(max_length=255)
  bio = models.TextField(max_length=500)
  privacy = models.BooleanField(default=False)

