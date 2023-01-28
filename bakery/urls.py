
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/login', views.view_login, name='login'),
]
