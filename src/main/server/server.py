from flask import Flask
from flask_cors import CORS
from src.main.routes.events_routes import event_route_bp
from src.models.settings.connection import db_connection

db_connection = db_connection

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)

