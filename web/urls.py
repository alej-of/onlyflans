from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ruta , donde la envio (el que hace el trabajo)
    path('', views.index , name='index'),
    path('about/', views.about , name='acerca'),
    path('welcome/', views.welcome, name='bienvenido'),
    path('contactUs/', views.contactUs, name='contacto'),
    path('contact_success/',views.success,name='exito'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update_account/', views.update_account, name='update_account'),
]