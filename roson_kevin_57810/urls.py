from django.contrib import admin
from django.urls import path, include
from roson_kevin_57810.views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('create/', create_view, name='create'),
    path('read/', read_view, name='read'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
