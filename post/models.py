from django.db import models
from account.models import User


class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='uploads/post/images/%Y/%m/%d/')
  body = models.TextField(max_length=4000)
  created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.title + 'By, ' +self.author)



