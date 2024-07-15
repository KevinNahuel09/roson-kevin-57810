import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('kevin.db')
c = conn.cursor()

# Crear la tabla de usuarios
c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insertar tres usuarios
usuarios = [
    ('kevin', 'kevin123'),
    ('agus', 'agus123'),
    ('peti', 'peti123')
]

c.executemany('INSERT INTO usuarios (username, password) VALUES (?, ?)', usuarios)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
