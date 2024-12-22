import pytest
from src.models.repository.events_repository import EventsRepository
from src.models.settings.connection import db_connection

db_connection = db_connection

@pytest.mark.skip(reason="New Register in database")
def test_insert_event():
    event = {
        "title": "Título do evento",
        "details": "Aqui ficará a descrição do evento ",
        "slug": "Slug é um texto que identifica o evento na URL",
        "maximum_attendees": 200, 
    }

    event_repository = EventsRepository()
    response = event_repository.insert_event(event)
    assert response is not None
    
def test_get_event_by_id():
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(1232)
