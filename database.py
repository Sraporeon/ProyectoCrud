import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )''')

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos creada exitosamente.")
