from django.shortcuts import render


def get_profile_page(request):
    return render(request, 'profiles/base.html')
