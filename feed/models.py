from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class PostEvent(models.Model):
  """
  Created when a user triggers a post event.
  """
  instigator = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='instigated_post_event')
  post = models.ForeignKey(
      Post, on_delete=models.CASCADE, related_name='post_event')
  created_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    """
    Data used to order events.
    """
    ordering = ['-created_on']
  
  def __str__(self):
    return f'${self.instigator} created a post on ${self.created_on}'
  
