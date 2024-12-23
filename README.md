# pass.in

O pass.in é uma aplicação de **gestão de participantes em eventos presenciais**.

A ferramenta permite que o organizador cadastre um evento e abra uma página pública de inscrição.

Os participantes inscritos podem emitir uma credencial para check-in no dia do evento.

O sistema fará um scan da credencial do participante para permitir a entrada no evento.

## Especificações

### Requisitos

#### Requisitos funcionais

- [ ] O organizador deve poder cadastrar um novo evento;
- [ ] O organizador deve poder visualizar dados de um evento;
- [ ] O organizador deve poder visualizar a lista de participantes;
- [ ] O participante deve poder se inscrever em um evento;
- [ ] O participante deve poder visualizar seu crachá de inscrição;
- [ ] O participante deve poder realizar check-in no evento;

#### Regras de negócio

- [ ] O participante só pode se inscrever em um evento uma única vez;
- [ ] O participante só pode se inscrever em eventos com vagas disponíveis;
- [ ] O participante só pode realizar check-in em um evento uma única vez;

#### Requisitos não-funcionais

- [ ] O check-in no evento será realizado através de um QRCode;

## Configuração do Banco de Dados

Para configurar a conexão com o banco de dados MSSQL, siga os passos abaixo:

1. Crie um arquivo `auth.ini` na raiz do projeto com o seguinte conteúdo:

    ```ini
    [database]
    server = your_server_name
    database = your_database_name
    username = your_username
    password = your_password
    ```

2. Certifique-se de que a estrutura de diretórios está correta:

    ```
    D:/WorkspaceProgramming/RocketSeat/Python/NLW-15-Unite-Python/
    │
    ├── src/
    │   ├── main/
    │   │   ├── routes/
    │   │   │   └── events_routes.py
    │   │   └── server/
    │   │       └── server.py
    │   ├── models/
    │   │   ├── entities/
    │   │   │   ├── __init__.py
    │   │   │   ├── events.py
    │   │   │   ├── teste.py
    │   │   │   └── attendees.py
    │   │   ├── repository/
    │   │   │   ├── events_repository.py
    │   │   │   ├── teste_repository.py
    │   │   │   ├── events_repository_test.py
    │   │   │   └── teste_repository_test.py
    │   │   └── settings/
    │   │       ├── __init__.py
    │   │       ├── connection.py
    │   │       └── create_tables.py
    │   ├── data/
    │   │   └── event_handler.py
    │   ├── http_types/
    │   │   ├── http_request.py
    │   │   └── http_response.py
    │   └── __init__.py
    └── auth.ini
    ```

3. O arquivo `connection.py` deve conter o seguinte código para configurar a conexão com o banco de dados usando SQLAlchemy:

    ```python
    import configparser
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    def get_credentials():
        config = configparser.ConfigParser()
        config.read('auth.ini')
        return {
            'server': config['database']['server'],
            'database': config['database']['database'],
            'username': config['database']['username'],
            'password': config['database']['password']
        }

    credentials = get_credentials()
    DATABASE_URL = f"mssql+pyodbc://{credentials['username']}:{credentials['password']}@{credentials['server']}/{credentials['database']}?driver=ODBC+Driver+17+for+SQL+Server"

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    class DatabaseSession:
        def __enter__(self):
            self.session = SessionLocal()
            return self.session

        def __exit__(self, exc_type, exc_value, traceback):
            self.session.close()

    db_connection = DatabaseSession()
    ```

4. O arquivo `events.py` deve conter o seguinte código para definir o modelo de entidade `Events`:

    ```python
    from sqlalchemy import Column, String, Integer
    from src.models.settings import Base

    class Events(Base):
        __tablename__ = 'events'
        __table_args__ = {'schema': 'nlw_events'}

        id = Column(String, primary_key=True, index=True)
        title = Column(String, index=True)
        details = Column(String)
        slug = Column(String, unique=True, index=True)
        maximum_attendees = Column(Integer)
    ```

5. O arquivo `events_repository.py` deve conter o seguinte código para implementar o repositório usando SQLAlchemy:

    ```python
    from typing import Dict
    from src.models.settings.connection import db_connection
    from src.models.entities.events import Events
    from sqlalchemy.exc import IntegrityError

    class EventsRepository:
        def insert_event(self, eventsInfo: Dict) -> Dict:
            with db_connection as session:
                try:
                    event = Events(
                        id=eventsInfo.get('uuid'),
                        title=eventsInfo.get('title'),
                        details=eventsInfo.get('details'),
                        slug=eventsInfo.get('slug'),
                        maximum_attendees=eventsInfo.get('maximum_attendees')
                    )
                    session.add(event)
                    session.commit()
                    return eventsInfo
                except IntegrityError:
                    session.rollback()
                    raise Exception("Evento já cadastrado")
                except Exception as e:
                    session.rollback()
                    raise e
    ```

6. O arquivo `events_repository_test.py` deve conter o seguinte código para testar o método `insert_event` usando `pytest`:

    ```python
    import sys
    import os
    import pytest

    # Adiciona o diretório raiz do projeto ao sys.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

    from src.models.repository.events_repository import EventsRepository

    @pytest.fixture
    def event_data():
        return {
            "uuid": "123",
            "title": "Teste",
            "details": "teste",
            "slug": "teste",
            "maximum_attendees": 10 
        }

    def test_insert_event(event_data):
        event_repository = EventsRepository()
        response = event_repository.insert_event(event_data)
        assert response["uuid"] == event_data["uuid"]
        assert response["title"] == event_data["title"]
        assert response["details"] == event_data["details"]
        assert response["slug"] == event_data["slug"]
        assert response["maximum_attendees"] == event_data["maximum_attendees"]

    if __name__ == "__main__":
        pytest.main()
    ```

7. O arquivo `events_routes.py` deve conter o seguinte código para definir a rota `/events` usando Flask:

    ```python
    from flask import Blueprint, jsonify, request
    from src.http_types.http_request import HttpRequest
    from src.http_types.http_response import HttpResponse
    from src.data.event_handler import EventHandler

    event_route_bp = Blueprint("event_route", __name__)

    @event_route_bp.route("/events", methods=["POST"])
    def create_events():
        event_data = request.json
        http_request = HttpRequest(body=event_data)
        event_handler = EventHandler()
        http_response = event_handler.register(http_request)

        return jsonify(http_response.body), http_response.status_code
    ```

8. O arquivo `server.py` deve conter o seguinte código para iniciar o servidor Flask:

    ```python
    from flask import Flask
    from flask_cors import CORS
    from src.main.routes.events_routes import event_route_bp

    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(event_route_bp)

    if __name__ == "__main__":
        app.run(debug=True)
    ```

9. Para criar as tabelas no banco de dados, execute o seguinte script:

    ```python
    from sqlalchemy import create_engine
    from src.models.settings import Base
    from src.models.entities.events import Events
    from src.models.entities.attendees import Attendees
    from src.models.settings.connection import DATABASE_URL

    engine = create_engine(DATABASE_URL)

    # Cria todas as tabelas definidas nos modelos
    Base.metadata.create_all(engine)
    ```

10. Execute o script para criar as tabelas:

    ```sh
    python src/models/settings/create_tables.py
    ```

11. Execute os testes usando `pytest`:

    ```sh
    pytest src/models/repository/events_repository_test.py
    ```

Agora, você está pronto para usar a classe `DatabaseSession` para gerenciar a conexão com o banco de dados e realizar operações CRUD. Certifique-se de que o banco de dados e as tabelas estão configurados corretamente antes de executar os testes.