import pyodbc
from .connection import get_credentials

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

    def close(self):
        self.cursor.close()
        self.connection.close()

    def teste(self):
        self.cursor.execute("SELECT [id],[teste] FROM [db_ROCKETSEAT].[dbo].[tbl_teste]")
        return self.cursor.fetchall()

# Exemplo de uso
if __name__ == "__main__":
    db = Database()
    result = db.teste()
    for row in result:
        print(row)
    db.close()