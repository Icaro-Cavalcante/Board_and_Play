from sqlalchemy import create_engine
from ..config_database import Config_database

config = Config_database()

class Database():
    def __init__(self):
        self.session = create_engine(config.DATABASE_URL, echo=config.DATABASE_ECHO)
        self.test_session = create_engine(config.TESTS_URL, echo=True)

    def conectar(self):
        return self.session.connect()
    
    def conectar_test(self):
        return self.test_session.connect()