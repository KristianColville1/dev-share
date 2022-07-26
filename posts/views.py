from django.shortcuts import render
from django.views import generic, View
from .models import Post


def get_posts(request):
    return render(request, 'posts/base.html')
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "posts/base.html"

