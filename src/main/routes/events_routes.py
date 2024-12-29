from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.data.event_handler import EventHandler 
"""
    A utilização do blueprint é uma forma de organizar as rotas da aplicação. Com ela,
    o flask consegue organizar as rotas de forma mais eficiente e escalável.

"""
event_route_bp = Blueprint("event_route", __name__)

#O decorator route é utilizado para definir uma rota na aplicação.
@event_route_bp.route("/create/event", methods=["POST"])
def create_events():
    event_data = request.json
    http_request = HttpRequest(body=event_data)
    event_habdler = EventHandler()
    http_response = event_habdler.register(http_request)

    return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events", methods=["GET"])
def get_events():
    event_handle = EventHandler()
    http_response = event_handle.get_all()
    return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event_by_id(event_id):
    http_request = HttpRequest(parm={ "event_id" : event_id})
    event_handle = EventHandler()
    http_reponse = event_handle.get_event_by_id(http_request)
    return jsonify(http_reponse.body), http_reponse.status_code