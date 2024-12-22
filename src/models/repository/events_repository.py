from typing import Dict
from src.models.settings.connection import db_connection
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError, NoResultFound

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection as database:
            try:
                event = Events(
                title=eventsInfo.get('title'),
                details=eventsInfo.get('details'),
                slug=eventsInfo.get('slug'),
                maximum_attendees=eventsInfo.get('maximum_attendees')
                )
                database.add(event)
                database.commit()
                return eventsInfo
            
            except IntegrityError as integrity_error:
                database.rollback()
                raise Exception("Evento já cadastrado")
            
            except Exception as exception:
                database.rollback()
                raise exception
        
    def get_event_by_id(self, event_id: int) -> Events:
        with db_connection as database:
           try:
                event = {
                database.query(Events)
                .filter(Events.id == event_id)
                .one()
                }
                return event
           except NoResultFound as no_result_found:
                return None
           

#O With utilizado aqui é como se fosse, no C#, o using, que é uma forma de garantir que o recurso seja liberado após o uso.
#Ou em Java, o try-with-resources, que também é uma forma de garantir que o recurso seja liberado após o uso.