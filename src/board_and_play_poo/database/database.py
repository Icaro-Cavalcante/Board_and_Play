from sqlalchemy import create_engine
from src.board_and_play_poo.config_database import Config_database

config = Config_database()

class Database():
    '''Classe que cuida da conexão do banco de dados.'''
    def __init__(self):
        self.session = create_engine(config.DATABASE_URL, echo=config.DATABASE_ECHO) # Conexão
        self.test_session = create_engine(config.TESTS_URL, echo=True) # Conexão para testes

    def conectar(self):
        '''Estabelecendo a conexão.'''
        return self.session.connect()
    
    def conectar_test(self):
        '''Estabelecendo a conexão para o banco de dados de testes.'''
        return self.test_session.connect()