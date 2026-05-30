from flask import Blueprint, request, jsonify
from db import get_conn

alojamiento_bp = Blueprint("alojamientos", __name__)

## ruta que realiza un get de los alojamientos para ser consumidos por el cliente.
@alojamiento_bp.route("/", methods=["GET"])
def get_all():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alojamientos WHERE activo = TRUE")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)

