from django.urls import path
from . import views
from posts.models import Post

urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
]