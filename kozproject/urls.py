from django.contrib import admin
from django.urls import path, include
from myapp.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='home'),
    path('hello/', include('myapp.urls')),
]