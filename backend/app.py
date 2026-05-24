from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

CORS(app)

from routes.auth_routes import auth_bp
from routes.reserva_routes import reserva_bp
from routes.alojamiento_routes import alojamiento_bp
from routes.dashboard_routes import dashboard_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(reserva_bp, url_prefix="/api/reservas")
app.register_blueprint(alojamiento_bp, url_prefix="/api/alojamientos")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

@app.route("/")
def home():
    return {"message": "API Vora Mar Glamping funcionando"}

if __name__ == "__main__":
    app.run()