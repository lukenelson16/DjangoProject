from django.urls import path
from . import  views

# URLConf module (URL Configuration)
urlpatterns = [
    path('hello/', views.greeting)
]