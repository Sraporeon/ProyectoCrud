from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde el frontend

# Conexión a la base de datos
def conectar_db():
    return sqlite3.connect("productos.db")

# 1️⃣ Obtener todos los productos
@app.route("/productos", methods=["GET"])
def obtener_productos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    return jsonify([{"id": p[0], "nombre": p[1], "descripcion": p[2], "precio": p[3], "stock": p[4]} for p in productos])

# 2️⃣ Agregar un producto
@app.route("/productos", methods=["POST"])
def agregar_producto():
    data = request.json
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)", 
                   (data["nombre"], data["descripcion"], data["precio"], data["stock"]))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "Producto agregado"}), 201

# 3️⃣ Editar un producto
@app.route("/productos/<int:id>", methods=["PUT"])
def editar_producto(id):
    data = request.json
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id=?", 
                   (data["nombre"], data["descripcion"], data["precio"], data["stock"], id))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "Producto actualizado"}), 200

# 4️⃣ Eliminar un producto
@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "Producto eliminado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
