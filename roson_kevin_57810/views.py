from django.template import Template , Context, loader
from django.http import HttpResponse
from .models import Zapatilla
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import sqlite3
from django.views.decorators.csrf import csrf_protect

def saludar (request):
    saludo = "Bienvenidos al proyecto final de Roson"
    return HttpResponse(saludo)


def bienvenido(request):
    return render(request, 'bienvenido.html')


@csrf_protect
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Conectar a la base de datos y verificar las credenciales
        conn = sqlite3.connect('kevin.db')
        c = conn.cursor()
        c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        
        if user:
            return redirect('bienvenido')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
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

def read_view(request):
    zapatillas = Zapatilla.objects.all()
    return render(request, 'read.html', {'zapatillas': zapatillas})

def update_view(request):
    zapatillas = Zapatilla.objects.all()  
    if request.method == 'POST':
        
        nombre = request.POST.get('nombre')
        talle = request.POST.get('talle')
        color = request.POST.get('color')
        precio = request.POST.get('precio')

        for zapatilla in zapatillas:
            zapatilla.nombre = nombre
            zapatilla.talle = talle
            zapatilla.color = color
            zapatilla.precio = precio
            zapatilla.save()

        return redirect('read')  

    return render(request, 'update.html', {'zapatillas': zapatillas})


def delete_view(request):
    return render(request, 'delete.html')

# Obtener todas las zapatillas, Obtener datos del formulario, Actualizar todas las zapatillas

# def update(request):
#     zapatillas = Zapatilla.objects.all()  
#     if request.method == 'POST':
        
#         nombre = request.POST.get('nombre')
#         talle = request.POST.get('talle')
#         color = request.POST.get('color')
#         precio = request.POST.get('precio')

#         for zapatilla in zapatillas:
#             zapatilla.nombre = nombre
#             zapatilla.talle = talle
#             zapatilla.color = color
#             zapatilla.precio = precio
#             zapatilla.save()

#         return redirect('read')  

#     return render(request, 'update.html', {'zapatillas': zapatillas})

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

