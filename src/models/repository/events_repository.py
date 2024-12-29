from typing import Dict, List
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
                event = database.query(Events).filter(Events.id == event_id).one()
                
                if event is None: return None
                return [self._to_dict(event)]
           except NoResultFound as no_result_found:
                return None
           
    def get_all_events(self) -> List[Dict]: 
        with db_connection as database: 
            try:
                events = database.query(Events).all()
                '''
                o retorno da função get_all_events é uma lista de dicionários, onde cada dicionário representa um evento.
                '''
                return [self._to_dict(event) for event in events]

            except Exception as execption: 
                raise Exception(f"Houve um problema para recuperar os eventos. Erro: {execption}")
            
    

    def _to_dict(self, event: Events) -> Dict:
        """
        Método privado que converte um objeto do tipo Events em um dicionário.
        """
        return {
            "id": event.id,
            "title": event.title,
            "details": event.details,
            "slug": event.slug,
            "maximum_attendees": event.maximum_attendees
        }

#O With utilizado aqui é como se fosse, no C#, o using, que é uma forma de garantir que o recurso seja liberado após o uso.
#Ou em Java, o try-with-resources, que também é uma forma de garantir que o recurso seja liberado após o uso.