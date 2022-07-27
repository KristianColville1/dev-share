from tkinter import Widget
from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
  """
  Creates a post form for a given user.
  """
  class Meta:
    model = Post
    fields = ['title', 'body']
    widgets = {
      'title': forms.Textarea(attrs={
        'rows': 1,
        'placeholder': 'title of your post here'
      }),
      'body': forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Start writing your post here...'
      }),
    }