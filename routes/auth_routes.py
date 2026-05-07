from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_conn
from utils.functions_jwt import write_token, validate_token


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = get_conn()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(data["password"])
    cursor.execute("""
        INSERT INTO usuarios (nombre, email, pass) 
        VALUES (%s, %s, %s)
    """, (data["nombre"], data["email"], hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Usuario creado"})


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({
            "message": "Email y contraseña requeridos"
        }), 400

    conn = get_conn()
    if not conn:
        return jsonify({
            "message": "Error de conexión"
        }), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM usuarios WHERE email = %s",
        (email,)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        return jsonify({
            "message": "Usuario no encontrado"
        }), 404
    if not check_password_hash(user["pass"], password):
        return jsonify({
            "message": "Contraseña incorrecta"
        }), 401
    token = write_token(user)
    return jsonify({
        "message": "Login correcto",
        "token": token,
        "user": {
            "id": user["id"],
            "nombre": user["nombre"],
            "email": user["email"],
            "rol": user["rol"]
        }
    }), 200