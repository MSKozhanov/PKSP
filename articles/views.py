# from django.shortcuts import render

# from django.shortcuts import render

# def hello2(request):
#     return render(request, 'articles/archive.html',)

from django.shortcuts import render
from .models import Article  # Импортируем модель Article из вашего приложения

def hello2(request):
    articles = Article.objects.all()
    
    context = {'articles': articles}

    return render(request, 'articles/archive.html', context)
