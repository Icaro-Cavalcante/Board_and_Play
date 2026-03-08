from sqlalchemy import text

class Repository_venda():
    '''Classe que realiza as operações do banco de dados relacionadas a venda.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, venda):
        '''Recebe um objeto de venda e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            query = text ("""INSERT OR IGNORE INTO vendas
            (transacao_id, clientes_id, colaboradores_id, nota_fiscal)
            VALUES (:transacao_id, :clientes_id, :colaboradores_id, :nota_fiscal)""")

            conexao.execute (query, {"transacao_id":venda.id_transacao, "clientes_id":venda.id_cliente, "colaboradores_id":venda.id_colaborador, "nota_fiscal":venda.nota_fiscal} # Query
            )
            conexao.commit() # Commitando o cadastro
        return "Venda cadstrada"

    def read(self, id):
        '''Recebe o ID de uma venda e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM vendas WHERE id = :id""") # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            venda_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).first() # É retornada uma lista com uma tupla dentro
        if venda_bd: # Caso o venda exista
            return venda_bd # venda é retornado
        return None # Caso não, None é retornado