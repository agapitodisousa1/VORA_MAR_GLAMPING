from flask import request, jsonify
from utils.functions_jwt import validate_token


def get_current_user():

    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    try:
        token = auth_header.split(" ")[1]
    except:
        return None
    data = validate_token(token)
    if not data:
        return None

    return data


def admin_required():

    user = get_current_user()
    if not user:
        return None
    if user["rol"] != "admin":
        return None

    return user

def login_required():

    user = get_current_user()
    if not user:
        response = jsonify({
            "message": "No autenticado"
        })
        response.status_code = 401
        return response

    return user

