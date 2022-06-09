from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    datetime = models.DateTimeField()
    imageUrl = models.URLField(max_length=500)
    tags = models.ManyToManyField("Tag", related_name="posts")
  