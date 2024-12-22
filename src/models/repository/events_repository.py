from typing import Dict
from src.models.settings.connection import db_connection
from src.models.entities.events import Events

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection as database:
            event = Events(
                title=eventsInfo.get('title'),
                details=eventsInfo.get('details'),
                slug=eventsInfo.get('slug'),
                maximum_attendees=eventsInfo.get('maximum_attendees')
            )
            database.add(event)
            database.commit()
            return eventsInfo
        
    def get_event_by_id(self, event_id: int) -> Events:
        with db_connection as database:
            event = {
                database.query(Events)
                .filter(Events.id == event_id)
                .one()
            }
            return event