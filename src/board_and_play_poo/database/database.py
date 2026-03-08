from sqlalchemy import create_engine
from board_and_play_poo.modules.infrastructure.config_database import Config_database

config = Config_database()

class Database():
    '''Classe que cuida da conexão do banco de dados.'''
    def __init__(self, ambiente):
        self.session = create_engine(config.DATABASE_URL, echo=config.DATABASE_ECHO) # Conexão
        self.test_session = create_engine(config.TESTS_URL, echo=True) # Conexão para testes
        self.ambiente = ambiente

    def conectar(self):
        '''Estabelecendo a conexão.'''
        if self.ambiente == "teste":
            return self.test_session.connect()
        elif self.ambiente == "real":
            return self.session.connect()
        else:
            return None