from django.template import Template , Context, loader
from django.http import HttpResponse
from .models import Zapatilla
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import datetime

def saludar (request):
    saludo = "Bienvenidos al proyecto final de Roson"
    return HttpResponse(saludo)


def bienvenido(request):
    return render(request, 'bienvenido.html')


def home(request):
    with open('C:\\Users\\Morena\\Desktop\\roson-kevin-57810\\roson_kevin_57810\\plantillas\\home.html') as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)
    return HttpResponse(saludo)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bienvenido')  # Redirigir a la vista 'bienvenido'
        else:
            return HttpResponse("Usuario o contraseña incorrectos")
    return render(request, 'login.html')

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
    return render(request, 'update.html')

def delete_view(request):
    return render(request, 'delete.html')


def update(request):
    zapatillas = Zapatilla.objects.all()  # Obtener todas las zapatillas
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        talle = request.POST.get('talle')
        color = request.POST.get('color')
        precio = request.POST.get('precio')

        # Actualizar todas las zapatillas
        for zapatilla in zapatillas:
            zapatilla.nombre = nombre
            zapatilla.talle = talle
            zapatilla.color = color
            zapatilla.precio = precio
            zapatilla.save()

        return redirect('read')  

    return render(request, 'update.html', {'zapatillas': zapatillas})

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

