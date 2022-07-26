from django.shortcuts import render


def get_home_page(request):
    return render(request, 'home/home.html')

def get_home_logged_in(request):
    return render(request, 'home/logged_in.html')
