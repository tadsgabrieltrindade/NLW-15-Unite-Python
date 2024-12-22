from typing import Dict
from src.models.settings.connection import db_connection
from src.models.entities.teste import Teste

class TesteRepository:
    def insert_teste(self, testInfo: Dict) -> Dict:
        with db_connection as database:
            teste_registro = Teste(
                teste=testInfo.get('teste')
            )
            database.add(teste_registro)
            database.commit()
            return testInfo
        
    def get_all_testes(self) -> list:
        with db_connection as database:
            result = database.query(Teste).all()
            return [result.__dict__ for result in result]