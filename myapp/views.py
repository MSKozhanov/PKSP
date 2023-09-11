from django.shortcuts import render

def hello(request):
    return render(request, 'myapp/static_handler.html')
def init(request):
    return render(request, 'myapp/initial.html')