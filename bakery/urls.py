
from django.contrib import admin
from django.urls import path
from . import views
from productos.views import ProductListView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/login' , views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name="logout" ),
    path('productos/', include('productos.urls')),
]
