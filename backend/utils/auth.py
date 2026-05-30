from flask import request, jsonify
from utils.functions_jwt import validate_token

## funcion que identifica al usuario que hace la peticion al backend. Obtiene la cabecera
# authorization si no existe devuelve none. Luego extrae el token y lo valida mediante
# validate_token. Si es correcta la validacion devuelve la informacion contenida en el token.
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

## funcion que mira si el usuario tiene permisos de admin. obtiene el token de la cabecera
# Authorization y lo valida con validate_token, luego comprueba el campo rol. si no es admin
# devuelve none si es admin devuelve los datos del token.
def admin_required():

    auth = request.headers.get("Authorization")
    if not auth:
        
        return None

    token = auth.split(" ")[1]
    data = validate_token(token, output=True)
    if data["rol"] != "admin":

        return None

    return data

## funcion que verifica que el usuario esté autenticado mediante get_current_user, si no hay user
# devuelve codigo 401 unauthorized si hay user devuelve los datos del usuario
def login_required():

    user = get_current_user()
    if not user:
        response = jsonify({
            "message": "No autenticado"
        })
        response.status_code = 401
        return response

    return user

