from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
"""
    A utilização do blueprint é uma forma de organizar as rotas da aplicação. Com ela,
    o flask consegue organizar as rotas de forma mais eficiente e escalável.

"""
event_route_bp = Blueprint("event_route", __name__)

#O decorator route é utilizado para definir uma rota na aplicação.
@event_route_bp.route("/events", methods=["POST"])
def create_events():
    #Aqui é criado um objeto HttpRequest que será utilizado para encapsular a requisição
    http_request = HttpRequest(body=request.json)

    
    return jsonify({"Olá": "mundo"}), 200
