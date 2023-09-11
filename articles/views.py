from django.shortcuts import render

from django.shortcuts import render

def hello2(request):
    return render(request, 'articles/static_handler2.html')