from flask import Blueprint, request, jsonify
from db import get_conn

alojamiento_bp = Blueprint("alojamientos", __name__)

@alojamiento_bp.route("/", methods=["GET"])
def get_all():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alojamientos WHERE activo = TRUE")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)


@alojamiento_bp.route("/", methods=["POST"])
def create():
    data = request.json

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alojamientos (nombre, tipo, capacidad, precio_base)
        VALUES (%s, %s, %s, %s)
    """, (
        data["nombre"], data["tipo"], data["capacidad"], data["precio_base"]))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "alojamiento creado"})