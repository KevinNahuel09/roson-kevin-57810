"""
URL configuration for roson_kevin_57810 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roson_kevin_57810.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('create/', create_view, name='create'),
    path('read/', read_view, name='read'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
]
