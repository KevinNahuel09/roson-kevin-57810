from django.template import Template , Context, loader
from django.http import HttpResponse
from .models import Zapatilla
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import sqlite3
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError

def saludar (request):
    saludo = "Bienvenidos al proyecto final de Roson"
    return HttpResponse(saludo)


def bienvenido(request):
    return render(request, 'bienvenido.html')


@csrf_protect
def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # Autenticación de usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenido')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        
        elif action == 'register':
            new_username = request.POST.get('new_username')
            new_password = request.POST.get('new_password')
            
            try:
                # Crear el nuevo usuario
                User.objects.create_user(username=new_username, password=new_password)
                messages.success(request, 'Usuario registrado con éxito.')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya existe.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error: {e}')
        
        return redirect('home')
    
    return render(request, 'home.html')


def create_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        talle = request.POST.get('talle')
        color = request.POST.get('color')
        precio = request.POST.get('precio')
        
        Zapatilla.objects.create(nombre=nombre, talle=talle, color=color, precio=precio)
        return redirect('bienvenido')
    
    return render(request, 'create.html')

def register_view(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        
        if User.objects.filter(username=new_username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('home')
        
        user = User.objects.create_user(username=new_username, password=new_password)
        user.save()
        messages.success(request, 'Usuario registrado con éxito.')
        return redirect('home')
    
    return render(request, 'home.html')


def read_view(request):
    query = request.GET.get('q')
    
    if query:            
        zapatillas = Zapatilla.objects.filter(nombre__icontains=query)
    else:
        zapatillas = Zapatilla.objects.all()
    return render(request, 'read.html', {'zapatillas': zapatillas})

def update_view(request):
    zapatillas = Zapatilla.objects.all()
    if request.method == 'POST':
        zapatilla_id = request.POST.get('zapatilla_id')
        nombre = request.POST.get('nombre')
        talle = request.POST.get('talle')
        color = request.POST.get('color')
        precio = request.POST.get('precio')

        zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
        zapatilla.nombre = nombre
        zapatilla.talle = talle
        zapatilla.color = color
        zapatilla.precio = precio
        zapatilla.save()

        return redirect('read')

    return render(request, 'update.html', {'zapatillas': zapatillas})


def delete_view(request):
    zapatillas = Zapatilla.objects.all()
    if request.method == 'POST':
        zapatilla_id = request.POST.get('zapatilla_id')
        zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
        zapatilla.delete()

        return redirect('read')

    return render(request, 'delete.html', {'zapatillas': zapatillas})

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

