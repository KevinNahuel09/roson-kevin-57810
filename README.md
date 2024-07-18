# Proyecto Final de Roson - Comisión 57810
## Descripción del Proyecto
Este es el proyecto final desarrollado por Kevin Nahuel Roson para la comisión número 57810 del curso de Python. El proyecto consiste en una aplicación web básica para gestionar una colección de zapatillas, utilizando el framework Django.

Funcionalidades
La aplicación web permite realizar las siguientes acciones:

Crear Zapatilla: Permite añadir nuevas zapatillas a la base de datos especificando su nombre, talle, color y precio.
Ver Zapatillas: Muestra una lista de todas las zapatillas almacenadas en la base de datos.
Actualizar Zapatilla: Permite seleccionar una zapatilla existente y actualizar su información.
Eliminar Zapatilla: Permite eliminar una zapatilla de la base de datos.
Acerca de mí: Proporciona una breve descripción sobre el desarrollador del proyecto.
Tecnologías Utilizadas
Python: Lenguaje de programación principal.
Django: Framework web utilizado para el desarrollo de la aplicación.
SQLite: Base de datos utilizada para almacenar la información de las zapatillas.
HTML/CSS: Tecnologías utilizadas para la creación de las vistas de la aplicación.
Estructura del Proyecto
home.html: Página de inicio de la aplicación.
create.html: Página para crear nuevas zapatillas.
read.html: Página para ver la lista de zapatillas.
update.html: Página para actualizar la información de una zapatilla.
delete.html: Página para eliminar una zapatilla.
acerca_de_mi.html: Página con información sobre el desarrollador del proyecto.
Cómo Ejecutar el Proyecto
Clonar el repositorio:


`git clone https://github.com/tu_usuario/tu_repositorio.git`
Navegar al directorio del proyecto:


cd tu_repositorio
Crear y activar un entorno virtual:


python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instalar las dependencias:


pip install -r requirements.txt
Realizar las migraciones y ejecutar el servidor:


python manage.py migrate
python manage.py runserver
Información del Desarrollador
Hola, soy Kevin Nahuel Roson, estudiante de la comisión número 57810 de Python. Este es el primer curso de Python que hago. Tengo 31 años, soy de zona Sur del GBA y estoy muy expectante del resultado de este último TP.