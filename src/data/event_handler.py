from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class EventHandler: 
    def __init__(self) -> None:
        self.__event_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        event = http_request.body
        self.__event_repository.insert_event(event)
        return HttpResponse(body = {"Response: ": "Evento criado com sucesso!"}, status_code = 201)
