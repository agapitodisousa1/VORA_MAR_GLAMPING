from flask import Blueprint, request, jsonify
from db import get_conn
from datetime import datetime

reserva_bp = Blueprint("reservas", __name__)


## crea una reserva con post primero comprueba si hay conflicto con las reservas que ya hay 
# en la bd. luego se comprueba el precio base para poder calcular el precio total de la estancia.
# despues las fechas son convertidas a objetos tipo fecha mediante datetime.strptime().
# primero valida que la fecha sea posterior a la actual, luego valida que la de final sea posterior 
# a la actual. Una vez hecho esto se calcula la diferencia entre las dos fechas para establecer 
# la estancia. Despues se calcula el precio total. Al final se almacena en la bd con un insert into
# con estado pendiente y devuelve un 201 y el precio total.
@reserva_bp.route("/", methods=["POST"])
def crear_reserva():

    data = request.json
    conn = get_conn()
    if not conn:
        return jsonify({
            "message": "Error de conexión"
        }), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT *
        FROM reservas
        WHERE alojamiento_id = %s
        AND estado != 'cancelada'
        AND (
            fecha_inicio < %s
            AND fecha_fin > %s
        )
    """, (
        data["alojamiento_id"],
        data["fecha_fin"],
        data["fecha_inicio"]
    ))
    conflicto = cursor.fetchone()
    if conflicto:
        cursor.close()
        conn.close()
        return jsonify({
            "error": "Fechas no disponibles"
        }), 400
    cursor.execute("""
        SELECT precio_base
        FROM alojamientos
        WHERE id = %s
    """, (
        data["alojamiento_id"],
    ))
    alojamiento = cursor.fetchone()
    inicio = datetime.strptime(
        data["fecha_inicio"],
        "%Y-%m-%d"
    )
    fin = datetime.strptime(
        data["fecha_fin"],
        "%Y-%m-%d"
    )
    hoy = datetime.now()

    if inicio.date() < hoy.date():
        cursor.close()
        conn.close()
        return jsonify({
            "error": "No se pueden realizar reservas en fechas anteriores a la actual"
        }), 400
   
    if fin <= inicio:
        cursor.close()
        conn.close()
        return jsonify({
            "error": "Fechas inválidas"
        }), 400
    noches = (fin - inicio).days
    precio_total = (
        alojamiento["precio_base"]
        * noches
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservas (

            usuario_id,
            alojamiento_id,
            fecha_inicio,
            fecha_fin,
            precio_total,
            estado

        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            'pendiente'
        )
    """, (

        data["usuario_id"],
        data["alojamiento_id"],
        data["fecha_inicio"],
        data["fecha_fin"],
        precio_total

    ))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "message": "Reserva creada",
        "precio_total": precio_total
    }), 201

## realiza un get a todas las reservas.
@reserva_bp.route("/", methods=["GET"])
def get_reservas():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservas")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)
## realiza un get a las reserva del usuario actual ordenado por fecha de inicio.
@reserva_bp.route("/reserva/<int:id>", methods=["GET"])
def get_mis_reservas(id):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservas JOIN alojamientos ON reservas.alojamiento_id = alojamientos.id WHERE reservas.usuario_id = %s ORDER BY reservas.fecha_inicio DESC", (id,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(data)


## realiza un put es decir un update con el id pasado en la ruta y actualiza el estado a cancelada.
@reserva_bp.route("/<int:id>", methods=["PUT"])
def cancelar_reserva(id):

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservas
        SET estado = 'cancelada'
        WHERE id = %s
    """, (id, ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "Reserva cancelada"
    })

