from django.contrib import admin
from django.urls import path, include
from myapp.views import hello
from myapp.views import init
from articles.views import hello2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', init, name='init'),
    path('hello/', include('myapp.urls')),
    path('articles/', include('articles.urls')),
    
    
]