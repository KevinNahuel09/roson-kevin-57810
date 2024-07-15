from django.template import Template , Context, loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import datetime

def saludar (request):
    saludo = "Bienvenidos al proyecto final de Roson"
    return HttpResponse(saludo)


def bienvenido(request):
    saludo = f"Bienvenido al proyecto final"
    return HttpResponse(saludo)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1> Bienvenidos al curso de Django!</h1>
    <h2>Te damos la bienvenida {apellido} {nombre}</h2>
    <h3>Hoy es {hoy}</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("C:/Users/Morena/Desktop/roson_kevin_57810/roson_kevin_57810/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto) 
    return HttpResponse(saludo)

def bienvenido_tpl2(request):
    hoy = datetime.datetime.now()
    nombre = "Martin"
    apellido = "Palermo"
    Notas = [4,6,7]
    contexto = {"nombre": nombre, "apellido": apellido , "hoy": hoy, "Notas": Notas}
    plantilla = loader.get_template("bienvenido_tpl.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

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
    return render(request, 'create.html')

def read_view(request):
    return render(request, 'read.html')

def update_view(request):
    return render(request, 'update.html')

def delete_view(request):
    return render(request, 'delete.html')