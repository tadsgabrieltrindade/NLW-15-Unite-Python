import configparser

def get_credentials():
    config = configparser.ConfigParser()
    config.read('auth.ini')
    credentials = {
        'server' : config['database']['server'],
        'database' : config['database']['database'],
        'username': config['database']['Username'],
        'password': config['database']['Password']
    }
    return credentials