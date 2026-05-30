from jwt import decode, encode, exceptions
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta
 
## funcion que crea el token pasandole data en forma de diccionario.
## dentro del token se incluyen id, rol y fecha de expiracion.
## establece la expiración en 1 dia, obtiene la key desde las variables de entorno 
## y el algoritmo de encriptación es HS256
def write_token(data:dict):

    token = encode(payload={"user_id":data["id"], "rol":data["rol"], "exp" : datetime.now(tz=timezone.utc)+ timedelta(days=1)}, key=getenv("SECRET_KEY"), algorithm="HS256")

    return token

## funcion que comprueba la validez del token enviado desde el cliente.
# si output es false se verifica que el token sea valido. 
# si output es true se verifica el token y se devuelve los datos del usuario.   
# si el token es invalido se devuelve un mensaje de invalid token y respuesta 401 unauthroized.
# si el token ha expirado se devuelv un mensaje token expired y 401 unauthorized.
def validate_token(token, output=False):
    try:
        if output:
           return decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError as e:
        response = jsonify({"message":"Invalid Token"})
        response.status_code = 401

        return response
    except exceptions.ExpiredSignatureError as e:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401

        return response
    
