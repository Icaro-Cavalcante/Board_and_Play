from sqlalchemy import text
from datetime import datetime
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_transacao import RepositoryTransacao
from src.board_and_play_poo.repositories.repository_venda import RepositoryVenda
from src.board_and_play_poo.modules.domain.vendas import Venda

class RepositoryItemVenda():
    '''Classe que realiza as operações do banco de dados relacionadas a item_venda'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.transacao_repo = RepositoryTransacao(self.database, self.table)
        self.venda_repo = RepositoryVenda(self.database, self.table)


# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, item_venda):
        '''Recebe uma tupla com dados de item venda e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO itens_venda
            (venda_id, produto_id, quantidade_venda, preco_unitario)
            VALUES (:venda_id, :produto_id, :quantidade_venda, :preco_unitario)RETURNING id""") # Query

            aux = conexao.execute (query, {"venda_id":item_venda[0], "produto_id":item_venda[1], "quantidade_venda":item_venda[2], "preco_unitario":item_venda[3]} # Executando a query
            )
            id = aux.fetchone()[0]
            conexao.commit() # Commitando o cadastro
            return id

        else: # Se não
            return "Não foi possível conectar"

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
                return tupla # ItemVenda é retornado
        else:
            return None # Caso não, None é retornado
        
    def gerar_venda(self, lista_IV, comprovante, ForPagmt,  nota_fiscal, cliente_id, colaborador_id):
        '''Recebe uma lista de Jogos_venda (também uma lista, com todos os atributos, menos transacao_id, em ordem de criação) e cadastra uma venda no banco de dados'''
        soma = 0
        sum = 0
        tupla_transacao = (comprovante, None, ForPagmt, "VENDA")
        trans_id = self.transacao_repo.create(tupla_transacao)
        venda_obj = Venda(cliente_id, colaborador_id, nota_fiscal, comprovante, datetime.now(), None, ForPagmt, "VENDA", trans_id)
        venda_id = self.venda_repo.create(venda_obj)
        for item in lista_IV:
            tupla_item = (venda_id, item[0], item[1], item[2])
            self.create(tupla_item)
            soma += Venda.calcular_valor(item[2], item[1])
            sum += 1
        self.transacao_repo.update(trans_id, "valor_total", soma)
        return sum
