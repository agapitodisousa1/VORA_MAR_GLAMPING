from flask import Blueprint, request, jsonify
from db import get_conn

reserva_bp = Blueprint("reservas", __name__)

@reserva_bp.route("/", methods=["POST"])
def crear_reserva():
    data = request.json
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM reservas
        WHERE alojamiento_id = %s
        AND estado != 'cancelada'
        AND ( fecha_inicio < %s AND fecha_fin > %s)""", (data["alojamiento_id"], data["fecha_fin"], data["fecha_inicio"]))
    conflicto = cursor.fetchone()
    if conflicto:
        cursor.close()
        conn.close()
        return jsonify({"error": "Fechas no disponibles"}), 400
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservas (usuario_id, alojamiento_id, fecha_inicio, fecha_fin, estado)
        VALUES (%s, %s, %s, %s, 'pendiente')
    """, (data["usuario_id"], data["alojamiento_id"], data["fecha_inicio"], data["fecha_fin"])) 
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "reserva creada"})

@reserva_bp.route("/", methods=["GET"])
def get_reservas():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservas")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)