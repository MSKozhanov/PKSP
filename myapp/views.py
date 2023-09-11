from django.shortcuts import render

def hello(request):
    return render(request, 'myapp/static_handler.html')