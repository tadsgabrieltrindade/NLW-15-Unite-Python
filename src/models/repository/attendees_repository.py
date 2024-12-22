from typing import Dict
from src.models.settings.connection import db_connection
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError, NoResultFound

class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection as database:
            try:
                attendee = Attendees(
                name=attendee_info.get('name'),
                email=attendee_info.get('email'),
                event_id=attendee_info.get('event_id'),
                created_at=attendee_info.get('created_at')
                )
                database.add(attendee)
                database.commit()
                return attendee_info
            
            except IntegrityError as integrity_error:
                database.rollback()
                raise Exception("Atendimento já cadastrado")
            
            except Exception as exception:
                database.rollback()
                raise exception
        
    
    def get_attendee_by_id(self, attendee_id: int):
       
        """
            Recupera os detalhes de um participante pelo seu ID.
            Args:
                attendee_id (int): O ID do participante a ser recuperado.
            Retorna:
                dict: Um dicionário contendo o nome do participante, email e o título do evento que ele está participando.
                None: Se nenhum participante for encontrado com o ID fornecido.
            Métodos:
                .query: Inicia uma consulta na sessão do banco de dados.
                .join: Junta a tabela Attendees com a tabela Events com base no event_id.
                .filter: Filtra os resultados da consulta para corresponder ao attendee_id fornecido.
                .with_entities: Especifica as colunas a serem retornadas no resultado da consulta.
                .one: Executa a consulta e espera exatamente um resultado. Lança uma exceção se nenhum resultado for encontrado.
        """
        with db_connection as database:
           try:
                attendee = {
                database.query(Attendees)
                .join(Events, Attendees.event_id == Events.id)
                .filter(Attendees.id == attendee_id)
                .with_entities(
                    Attendees.name,
                    Attendees.email,
                    Events.title
                )
                .one()
                }
                return attendee
           except NoResultFound as no_result_found:
                return None
           

#O With utilizado aqui é como se fosse, no C#, o using, que é uma forma de garantir que o recurso seja liberado após o uso.
#Ou em Java, o try-with-resources, que também é uma forma de garantir que o recurso seja liberado após o uso.