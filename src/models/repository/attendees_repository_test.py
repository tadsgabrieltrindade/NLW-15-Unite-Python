import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection
from sqlalchemy.sql import func


db_connection = db_connection

@pytest.mark.skip(reason="New Register in database")
def test_insert_attendee():
    attendee_info = {
        'name': 'Teste',
        'email': 'teste@teste.com',
        'event_id': 1,
        'created_at': func.now()
    }	
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee_info)
    print(response)

def test_get_attendee_by_id():
    attendee_id = 1
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_by_id(attendee_id)
    print(response)