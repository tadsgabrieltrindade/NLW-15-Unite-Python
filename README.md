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
    ├── main.py
    └── sql/
        ├── conexao.py
        └── queries.py
    ```

3. O arquivo [main.py](http://_vscodecontentref_/0) deve conter o seguinte código para usar a classe [Database](http://_vscodecontentref_/1):

    ```python
    from sql.queries import Database

    # Exemplo de uso da classe Database
    db = Database()
    result = db.teste()
    for row in result:
        print(row)
    db.close()
    ```

4. O arquivo `conexao.py` deve conter o seguinte código para ler as credenciais do [auth.ini](http://_vscodecontentref_/2):

    ```python
    import configparser

    def get_credentials():
        config = configparser.ConfigParser()
        config.read('auth.ini')
        return {
            'server': config['database']['server'],
            'database': config['database']['database'],
            'username': config['database']['username'],
            'password': config['database']['password']
        }
    ```

5. O arquivo [queries.py](http://_vscodecontentref_/3) deve conter a classe [Database](http://_vscodecontentref_/4) com os métodos para realizar operações CRUD:

    ```python
    import pyodbc
    from sql.conexao import get_credentials

    class Database:
        def __init__(self):
            credentials = get_credentials()
            self.connection_string = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={credentials['server']};"
                f"DATABASE={credentials['database']};"
                f"UID={credentials['username']};"
                f"PWD={credentials['password']}"
            )
            self.connection = pyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()

        def fetch_all(self, query):
            self.cursor.execute(query)
            return self.cursor.fetchall()

        def fetch_one(self, query):
            self.cursor.execute(query)
            return self.cursor.fetchone()

        def execute(self, query):
            self.cursor.execute(query)
            self.connection.commit()

        def close(self):
            self.cursor.close()
            self.connection.close()

        def teste(self):
            self.cursor.execute("SELECT [id],[teste] FROM [db_ROCKETSEAT].[dbo].[tbl_teste]")
            return self.cursor.fetchall()
    ```

Agora, você está pronto para usar a classe [Database](http://_vscodecontentref_/5) para gerenciar a conexão com o banco de dados e realizar operações CRUD.