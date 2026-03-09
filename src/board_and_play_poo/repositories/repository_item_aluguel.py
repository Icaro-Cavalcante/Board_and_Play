from sqlalchemy import text
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test

class RepositoryItemAluguel():
    '''Classe que realiza as operações do banco de dados relacionadas a item aluguel'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, item_aluguel):
        '''Recebe uma tupla com dados de item aluguel e cadastra ela no banco de dados'''
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
            return "Não foi possível conectar"

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
                return tupla # ItemAluguel é retornado
        else:
            return None # Caso não, None é retornado

    def buscar_por_aluguel(self, id):
        '''Recebe o ID de um aluguel e retorna as tuplas dos item aluguel desse aluguel'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT * FROM itens_aluguel 
            WHERE itens_aluguel.aluguel_id = :id""")

            tuplas = conexao.execute (query, {"id": id, } # query
            ).all() # Recebe uma lista com as tuplas
            if tuplas:
                return tuplas # ItemAluguel é retornado
            else:
                return None
        else:
            return None # Caso não, None é retornado

    def imprimir_dados(self, tupla):
        '''Imprime dados de uma tupla de item aluguel, semelhante a uma função __str__'''
        dic_atributos = {1: "ID", 2: "ID de aluguel", 3: "ID de jogo", 4: "Valor da diária", 5: "Valor da sessão"}
        atributo_num = 1
        for atributo in tupla:
            print(f"{dic_atributos[atributo_num]}: {atributo}")
            atributo_num += 1
