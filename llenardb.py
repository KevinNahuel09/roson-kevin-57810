import sqlite3
import random

# Conexión a la base de datos
conn = sqlite3.connect('kevin.db')
c = conn.cursor()

# Creacion de la tabla de zapatillas
c.execute('''
    CREATE TABLE IF NOT EXISTS Zapatilla (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    talle INTEGER NOT NULL,
    color TEXT NOT NULL,
    precio REAL NOT NULL
);
''')

# Datos para la tabla
nombres = ['Zapatilla A', 'Zapatilla B', 'Zapatilla C', 'Zapatilla D', 
           'Zapatilla E', 'Zapatilla F', 'Zapatilla G', 'Zapatilla H', 
           'Zapatilla I', 'Zapatilla J']
colores = ['Rojo', 'Azul', 'Verde', 'Negro', 'Blanco', 'Amarillo', 
           'Gris', 'Naranja', 'Rosa', 'Marrón']

# Insertar datos para 10 tipos de zapatillas
zapatillas = [
    (nombres[i], random.randint(36, 45), random.choice(colores), round(random.uniform(50.0, 150.0), 2))
    for i in range(10)
]

c.executemany('INSERT INTO Zapatilla (nombre, talle, color, precio) VALUES (?, ?, ?, ?)', zapatillas)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
