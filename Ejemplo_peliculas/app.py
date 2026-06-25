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

@app.route('/peliculas', methods=['GET'])
def obtener_usuarios():

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, titulo, genero FROM peliculas"
    )

    datos = cursor.fetchall()

    peliculas = []

    for pelicula in datos:
        peliculas.append({
            "id": pelicula[0],
            "titulo": pelicula[1],
            "genero": pelicula[2]
        })

    cursor.close()

    return jsonify(peliculas)


@app.route('/peliculas/<int:id>', methods=['GET'])
def obtener_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, titulo, genero FROM peliculas WHERE id=%s",
        (id,)
    )

    pelicula = cursor.fetchone()

    cursor.close()

    if pelicula:
        return jsonify({
            "id": pelicula[0],
            "titulo": pelicula[1],
            "genero": pelicula[2]
        })

    return jsonify({
        "error": "Película no encontrada"
    }), 404


@app.route('/peliculas', methods=['POST'])
def crear_usuario():

    datos = request.get_json()

    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO peliculas(titulo, genero) VALUES(%s, %s) RETURNING id',
        (datos['titulo'], datos['genero'])
    )

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()

    return jsonify({
        'id': nuevo_id,
        'titulo': datos['titulo'],
        'genero': datos['genero']
    }), 201

@app.route('/peliculas/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        'DELETE FROM peliculas WHERE id=%s',
        (id,)
    )

    conexion.commit()

    cursor.close()

    return jsonify({
        'mensaje': 'Película eliminada correctamente'
    })


if __name__ == '__main__':
    app.run(debug=True)