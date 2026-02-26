class Config_database():
    '''Classe que configura o banco de dados.'''
    DATABASE_URL = 'sqlite:///src/board_and_play_poo/data/dados.db'
    DATABASE_ECHO = False
    TESTS_URL = 'sqlite:///src/board_and_play_poo/data_test/dados.db'