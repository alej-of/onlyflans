from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ruta , donde la envio (el que hace el trabajo)
    path('', views.index , name='index'),
    path('about/', views.about , name='acerca'),
    path('welcome/', views.welcome, name='bienvenido'),
]