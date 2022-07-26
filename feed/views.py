from django.shortcuts import render
from django.views import View, generic
from posts.models import Post

def get_feed(request):
  return render(request, 'feed/index.html')
class FeedView(generic.ListView):
  """
  Creates a class based view of the feed page after a user is logged in and
  authenticated.
  """
  model = Post
  queryset = Post.objects.filter(status=1).order_by("-created_on")
  template_name = "feed/index.html"