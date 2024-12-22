from src.models.repository.teste_repository import TesteRepository
from src.models.settings.connection import db_connection

db_connection = db_connection

def test_insert_teste():
    teste_registro = {
        "teste": "Olha Só"
    }

    teste_repository = TesteRepository()
    response = teste_repository.insert_teste(teste_registro)

def test_get_all_testes():
    teste_repository = TesteRepository()
    response = teste_repository.get_all_testes()