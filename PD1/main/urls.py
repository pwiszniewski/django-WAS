from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('programing/languages', views.programingLanguages, name='programingLanguages'),
]