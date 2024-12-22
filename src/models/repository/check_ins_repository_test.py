from src.models.entities import attendees, check_ins
from src.models.repository.check_ins_repository import CheckInRepository
from src.models.settings.connection import db_connection
from sqlalchemy.sql import func
import pytest


db_connection = db_connection


@pytest.mark.skip(reason="Inserção na tbl")
def test_insert_check_in():
    checkIn = {
        "created_at": func.now(),
        "attendeeID": 1
    }

    checkIn_repository = CheckInRepository()
    response = checkIn_repository.insert_check_in(checkIn)
    assert response is not None

def test_get_checkIn_by_id():
    checkIn_repository = CheckInRepository()
    response = checkIn_repository.get_checkIn_by_Id(1)
    print(response)