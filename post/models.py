from django.db import models
from account.models import User


def upload_path(instance, filename):
  return 'images/{0}/posts/{1}'.format(instance.author.username, filename)

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to=upload_path, blank=True, null=True)
  body = models.TextField(max_length=4000)
  created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "{title}- {author}".format(title=self.title, author=self.author)



