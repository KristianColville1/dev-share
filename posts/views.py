from django.shortcuts import render


def get_posts(request):
    return render(request, 'posts/base.html')
