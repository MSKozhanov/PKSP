# from django.shortcuts import render

# from django.shortcuts import render

# def hello2(request):
#     return render(request, 'articles/archive.html',)

from django.shortcuts import render
from .models import Article  
from django.shortcuts import render, get_object_or_404


def hello2(request):
    articles = Article.objects.all()
    
    context = {'articles': articles}

    return render(request, 'articles/archive.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})