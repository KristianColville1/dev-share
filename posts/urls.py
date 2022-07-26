from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
]