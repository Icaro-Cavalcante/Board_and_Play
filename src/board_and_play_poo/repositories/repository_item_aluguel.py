from sqlalchemy import text
from src.board_and_play_poo.modules.domain.jogos import Jogo
from src.board_and_play_poo.modules.domain.alugueis import Aluguel
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test

class Repository_item_aluguel():
    '''Classe que realiza as operações do banco de dados relacionadas a item aluguel.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

    def create(self, item_aluguel):
        '''Recebe uma tupla com dados de item aluguel e cadastra ela no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO itens_aluguel
            (aluguel_id, jogo_id, valor_diaria, valor_sessao)
            VALUES (:aluguel_id, :jogo_id, :valor_diaria, :valor_sessao)""") # Query

            conexao.execute (query, {"aluguel_id": item_aluguel[0], "jogo_id":item_aluguel[1], "valor_diaria":item_aluguel[2], "valor_sessao":item_aluguel[3]} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "Jogo aluguel cadastrado"

        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um item aluguel e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT * FROM itens_aluguel 
            WHERE itens_aluguel.id = :id""")

            tupla = conexao.execute (query, {"id": id, } # query
            ).first()
            if tupla:
                return  # Item_aluguel é retornado
        return None # Caso não, None é retornado