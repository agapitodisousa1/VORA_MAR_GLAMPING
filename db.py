import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    try:
        conexion= mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
        )
        if conexion.is_connected:
            return conexion
    except:
        print("Error de conexión a la bbdd")
        return 