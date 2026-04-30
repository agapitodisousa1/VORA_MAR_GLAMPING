from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_conn

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = get_conn()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(data["password"])
    cursor.execute("""
        INSERT INTO usuarios (nombre, email, password)
        VALUES (%s, %s, %s)
    """, (data["nombre"], data["email"], hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Usuario creado"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (data["email"],))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user and check_password_hash(user["password"], data["password"]):
        return jsonify({
            "message": "login correcto",
            "user": user
        })

    return jsonify({"error": "credenciales incorrectas"}), 401