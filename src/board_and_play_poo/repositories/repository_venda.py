from sqlalchemy import text
from src.board_and_play_poo.modules.domain.vendas import Venda
from src.board_and_play_poo.repositories.repository_transacao import RepositoryTransacao

class RepositoryVenda():
    '''Classe que realiza as operações do banco de dados relacionadas a venda'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.transacao_repo = RepositoryTransacao(self.database, self.table)

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, venda):
        '''Recebe um objeto de venda e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao:
            query = text ("""INSERT OR IGNORE INTO vendas
            (transacao_id, cliente_id, colaborador_id, nota_fiscal)
            VALUES (:transacao_id, :cliente_id, :colaborador_id, :nota_fiscal)""")

            aux = conexao.execute (query, {"transacao_id":venda.id_transacao, "cliente_id":venda.id_cliente, "colaborador_id":venda.id_colaborador, "nota_fiscal":venda.nota_fiscal} # Query
            )
            id = aux.lastrowid
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return id
        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de uma venda e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao:
            query = text ("""SELECT * FROM vendas WHERE id = :id""") # query
            venda_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).first() # É retornada uma lista com uma tupla dentro
            if venda_bd: # Caso o venda exista
                return venda_bd # venda é retornado
            return None # Caso não, None é retornado
        else:
            return None # Caso não, None é retornado
        
    def read_especifico(self, atributo, status):
        conexao = self.database.conectar()
        if conexao:
            query = text(f"""SELECT * FROM vendas WHERE {atributo} = :status""")
            tupla = conexao.execute (query, {"status": status,}).all()
            if tupla:
                lista = []
                for tuple in tupla:
                    aux = self.tupla_objeto(tuple)
                    lista.append(aux)
                return lista
            else:
                return None

    def tupla_objeto(self, obj):
        tupla_trns = self.transacao_repo.read(obj.transacao_id)
        return Venda(obj[2], obj.colaborador_id, obj.nota_fiscal, tupla_trns[1], tupla_trns[2], tupla_trns[3], tupla_trns[4], tupla_trns[5], tupla_trns[0], obj.id)