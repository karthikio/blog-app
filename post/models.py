from django.db import models
from account.models import User

def post_upload_path(instance, filename):
    return 'uploads/posts/images/%Y/%m/%d/' % (instance.user.user.username, filename)


class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to=post_upload_path)
  body = models.TextField(max_length=4000)
  created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.title + 'By, ' +self.author)



