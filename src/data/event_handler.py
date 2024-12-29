from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

"""
    Essa classe é responsável por lidar com os eventos que são recebidos pelo servidor.
    Ela recebe um evento, e o insere no banco de dados, atraves do repositório de eventos.
"""

class EventHandler: 
    def __init__(self) -> None:
        self.__event_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        event = http_request.body
        self.__event_repository.insert_event(event)
        return HttpResponse(body = {"Response ": "Evento criado com sucesso!"}, status_code = 201)

    def get_all(self) -> HttpResponse:
        list_events = self.__event_repository.get_all_events()
        return HttpResponse(body={"events ": list_events}, status_code=200)
    
    def get_event_by_id(self, http_Request: HttpRequest) -> HttpResponse:
        event_id = http_Request.parm["event_id"]
        event = self.__event_repository.get_event_by_id(event_id)
        return HttpResponse(body = { "event": event }, status_code=200)
        