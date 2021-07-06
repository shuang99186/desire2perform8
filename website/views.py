from django.shortcuts import render

def programs(request):
    return render(request, 'web/programs.html', {})


def home(request):
    return render(request, 'web/home.html', {})