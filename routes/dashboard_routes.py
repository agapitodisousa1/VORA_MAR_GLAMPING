from flask import Blueprint, jsonify
from db import get_conn
from utils.auth import admin_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/", methods=["GET"])
def dashboard():

    user = admin_required()
    if not user:
        return jsonify({
            "message": "No autorizado"
        }), 401
    conn = get_conn()
    if not conn:
        return jsonify({
            "message": "Error de conexión"
        }), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT COUNT(*) AS total_reservas
        FROM reservas
    """)
    total_reservas = cursor.fetchone()["total_reservas"]
    cursor.execute("""
        SELECT SUM(precio_total) AS ingresos
        FROM reservas
        WHERE estado = 'confirmada'
    """)
    ingresos = cursor.fetchone()["ingresos"] or 0
    cursor.execute("""
        SELECT COUNT(*) AS total_usuarios
        FROM usuarios
    """)
    total_usuarios = cursor.fetchone()["total_usuarios"]
    cursor.execute("""
        SELECT COUNT(*) AS total_alojamientos
        FROM alojamientos
    """)
    total_alojamientos = cursor.fetchone()["total_alojamientos"]
    cursor.close()
    conn.close()
    return jsonify({
        "total_reservas": total_reservas,
        "ingresos": float(ingresos),
        "total_usuarios": total_usuarios,
        "total_alojamientos": total_alojamientos
    })