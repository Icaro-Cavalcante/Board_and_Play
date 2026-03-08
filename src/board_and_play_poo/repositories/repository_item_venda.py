from sqlalchemy import text
from src.board_and_play_poo.modules.domain.jogos import Jogo
from src.board_and_play_poo.modules.domain.vendas import Venda
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test

class Repository_item_venda():
    '''Classe que realiza as operações do banco de dados relacionadas a item_venda.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------- CRUD -------------------------------------------

    def create(self, item_venda):
        '''Recebe uma tupla com dados de item venda e cadastra ele no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO itens_venda
            (venda_id, produto_id, quantidade_id, preco_unitario)
            VALUES (:venda_id, :produto_id, :quantidade_id, :preco_unitario)""") # Query

            conexao.execute (query, {"venda_id":item_venda[0], "produto_id":item_venda[1], "quantidade_id":item_venda[2], "preco_unitario":item_venda[3]} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "item_venda cadastrado"

        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um item_venda e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT * FROM itens_venda 
            WHERE itens_venda.id = :id""")

            tupla = conexao.execute (query, {"id": id, } # query
            ).first()
            if tupla:
                return  # Item_venda é retornado
        return None # Caso não, None é retornado