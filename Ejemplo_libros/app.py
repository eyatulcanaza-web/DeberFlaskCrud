from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conexion = psycopg2.connect(
    host="localhost",
    database="Curso_Flask",   
    user="postgres",
    password="12345",         
    port="5432"
)

print("Conexión exitosa")

@app.route('/libros', methods=['GET'])
def obtener_usuarios():

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, titulo, autor FROM libros"
    )

    datos = cursor.fetchall()

    libros = []

    for libro in datos:
        libros.append({
            "id": libro[0],
            "titulo": libro[1],
            "autor": libro[2]
        })

    cursor.close()

    return jsonify(libros)


@app.route('/libros/<int:id>', methods=['GET'])
def obtener_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, titulo, autor FROM libros WHERE id=%s",
        (id,)
    )

    libro = cursor.fetchone()

    cursor.close()

    if libro:
        return jsonify({
            "id": libro[0],
            "titulo": libro[1],
            "autor": libro[2]
        })

    return jsonify({
        "error": "Libro no encontrado"
    }), 404


@app.route('/libros', methods=['POST'])
def crear_usuario():

    datos = request.get_json()

    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO libros(titulo, autor) VALUES(%s, %s) RETURNING id',
        (datos['titulo'], datos['autor'])
    )

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()

    return jsonify({
        'id': nuevo_id,
        'titulo': datos['titulo'],
        'autor': datos['autor']
    }), 201


@app.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        'DELETE FROM libros WHERE id=%s',
        (id,)
    )

    conexion.commit()

    cursor.close()

    return jsonify({
        'mensaje': 'Libro eliminado correctamente'
    })


if __name__ == '__main__':
    app.run(debug=True)