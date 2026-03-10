from sqlalchemy import text
from datetime import datetime
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
            VALUES (:venda_id, :produto_id, :quantidade_venda, :preco_unitario)""") # Query

            aux = conexao.execute (query, {"venda_id":item_venda[0], "produto_id":item_venda[1], "quantidade_venda":item_venda[2], "preco_unitario":item_venda[3]} # Executando a query
            )
            id = aux.lastrowid
            conexao.commit() # Commitando o cadastro
            conexao.close()
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
        
    def buscar_por_venda(self, id):
        '''Recebe o ID de uma venda e retorna as tuplas dos item venda dessa venda'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT * FROM itens_venda 
            WHERE itens_venda.venda_id = :id""")

            tuplas = conexao.execute (query, {"id": id, } # query
            ).all() # Recebe uma lista com as tuplas
            conexao.close()
            if tuplas:
                return tuplas # ItemVenda é retornado
            else:
                return None
        else:
            conexao.close()
            return None # Caso não, None é retornado
        
    def imprimir_dados(self, tupla):
        '''Imprime dados de uma tupla de item venda, semelhante a uma função __str__'''
        dic_atributos = {1: "ID", 2: "ID de venda", 3: "ID de jogo", 4: "Quantidade na venda", 5: "Preço unitário"}
        atributo_num = 1
        for atributo in tupla:
            print(f"{dic_atributos[atributo_num]}: {atributo}")
            atributo_num += 1
        
    def gerar_venda(self, lista_IV, comprovante, ForPagmt, nota_fiscal, cliente_id, colaborador_id):
        '''Método para'''
        total_venda = 0
        tupla_transacao = (comprovante, total_venda, ForPagmt, "VENDA")
        trans_id = self.transacao_repo.create(tupla_transacao)
        if trans_id:
            venda_obj = Venda(cliente_id, colaborador_id, nota_fiscal, comprovante, datetime.now(), 0, ForPagmt, "VENDA", trans_id)
            venda_id = self.venda_repo.create(venda_obj)
            if venda_id:
                for item in lista_IV:
                    tupla_item = (venda_id, item[0], item[1], item[2])
                    total_venda = total_venda + (item[1] * item[2])
                    self.create(tupla_item)
                self.transacao_repo.update(trans_id, "valor_total", total_venda)
                return trans_id
        return None