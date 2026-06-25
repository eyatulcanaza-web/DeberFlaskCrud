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

@app.route('/mascotas', methods=['GET'])
def obtener_usuarios():

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre, especie FROM mascotas"
    )

    datos = cursor.fetchall()

    mascotas = []

    for mascota in datos:
        mascotas.append({
            "id": mascota[0],
            "nombre": mascota[1],
            "especie": mascota[2]
        })

    cursor.close()

    return jsonify(mascotas)


@app.route('/mascotas/<int:id>', methods=['GET'])
def obtener_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre, especie FROM mascotas WHERE id=%s",
        (id,)
    )

    mascota = cursor.fetchone()

    cursor.close()

    if mascota:
        return jsonify({
            "id": mascota[0],
            "nombre": mascota[1],
            "especie": mascota[2]
        })

    return jsonify({
        "error": "Mascota no encontrada"
    }), 404


@app.route('/mascotas', methods=['POST'])
def crear_usuario():

    datos = request.get_json()

    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO mascotas(nombre, especie) VALUES(%s, %s) RETURNING id',
        (datos['nombre'], datos['especie'])
    )

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()

    return jsonify({
        'id': nuevo_id,
        'nombre': datos['nombre'],
        'especie': datos['especie']
    }), 201



@app.route('/mascotas/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        'DELETE FROM mascotas WHERE id=%s',
        (id,)
    )

    conexion.commit()

    cursor.close()

    return jsonify({
        'mensaje': 'Mascota eliminada correctamente'
    })


if __name__ == '__main__':
    app.run(debug=True)