from django.contrib import admin
from django.urls import path, include
from roson_kevin_57810.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('create/', create_view, name='create'),
    path('read/', read_view, name='read'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
]
