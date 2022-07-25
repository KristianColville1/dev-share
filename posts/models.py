from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
  title = models.TextField(max_length=80)
  slug = models.SlugField(unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
  post = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  
  
