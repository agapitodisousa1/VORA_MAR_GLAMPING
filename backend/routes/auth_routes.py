from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_conn
from utils.functions_jwt import write_token, validate_token


auth_bp = Blueprint("auth", __name__)

## ruta que realiza un post a la api que comprueba que haya conexion a la bbdd,
# comprueba que el usuario no exista y si no existe realiza el insert into a la bbdd
# con los datos, es decir nombre, email, password que es hasheado, telefono y rol. 
@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        conn = get_conn()
        if not conn:
            return jsonify({
                "message": "Error de conexión"
            }), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s",
            (data["email"],)
        )
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            conn.close()
            return jsonify({
                "message": "El correo ya está registrado"
            }), 400
        hashed_password = generate_password_hash(
            data["password"]
        )
        cursor.execute("""
            INSERT INTO usuarios (
                nombre,
                email,
                pass,
                telefono,
                rol
            )
            VALUES (%s, %s, %s, %s, %s)
        """, ( data["nombre"], data["email"], hashed_password, data["telefono"], "cliente"))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({
            "message": "Usuario creado"
        }), 201

    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500

# ruta que hace inicio de sesion. comprueba que email y password hayan sido introducidos,
# devuelve una respuesta 500 si no hay conexion a la bbdd, comprueba que exista primero usuario
# y luego contraseña y si la hay genera un token con write_token, y devuelve el user con su id,
# rol, email y nombre.
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