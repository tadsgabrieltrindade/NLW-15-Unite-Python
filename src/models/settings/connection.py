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