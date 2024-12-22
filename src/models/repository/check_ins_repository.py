from src.models.entities.check_ins import CheckIn
from src.models.entities.attendees import Attendees
from src.models.settings.connection import db_connection
from typing import Dict
from sqlalchemy.exc import IntegrityError, NoResultFound


class CheckInRepository():
    def insert_check_in(self, checkInInfo: Dict) -> Dict:
        with db_connection as database:
            try:
                checkIn = CheckIn(
                    created_at=checkInInfo.get("created_at"),
                    attendeeID=checkInInfo.get("attendeeID")
                )
                database.add(checkIn)
                database.commit()
                return checkIn
            
            except IntegrityError as integrity_error:
                database.rollback()
                raise Exception("Check In já feito")
            
            except Exception as exception:
                database.rollback()
                raise exception
            
    def get_checkIn_by_Id(self, chekIn_id) -> CheckIn:
        with db_connection as database: 
            try:
                checkIn_result = {
                    database.query(CheckIn)
                    .join(Attendees, CheckIn.attendeeID == Attendees.id)
                    .filter(CheckIn.Id == chekIn_id)
                    .with_entities(
                        CheckIn.Id,
                        CheckIn.created_at,
                        Attendees.id,
                        Attendees.name,
                        Attendees.email
                    )
                    .one()
                    
                }
                
                return checkIn_result
                

            except NoResultFound as exception: 
                return None
            
            except Exception as exception:
                raise exception