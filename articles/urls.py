from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello2, name='hello2'),
]