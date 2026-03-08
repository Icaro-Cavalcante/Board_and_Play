from sqlalchemy import text
from ..modules.domain.vendas import Venda

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
        print("Venda cadastrada.")

    def read(self, id):
        '''Recebe o ID de uma venda e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM vendas WHERE id = :id""") # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            venda_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).all() # É retornada uma lista com uma tupla dentro
        venda_bd = venda_bd[0] # Pega a tupla da lista

        if venda_bd: # Caso o venda exista
            venda = Venda(venda_bd[1], venda_bd[2], venda_bd[3], venda_bd[4], venda_bd[0]) # Transformando venda em um objeto
            return venda # venda é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, clientes_id_atributo, atributo_update):
        '''Recebe o ID de um venda, o clientes_id do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        query = text (f'''UPDATE vendas
                    SET {clientes_id_atributo} = {atributo_update}
                    WHERE id = {id}''')
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (query)
            conexao.commit()
            
        print("Atributo atualizado.")

# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, venda):
        '''Recebe um objeto de Venda e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            query = text ("""INSERT OR IGNORE INTO vendas
            (transacao_id, clientes_id, colaboradores_id, nota_fiscal)
            VALUES (:transacao_id, :clientes_id, :colaboradores_id, :nota_fiscal)""") # Query

            conexao.execute (query, {"transacao_id":venda.id_transacao, "clientes_id":venda.id_cliente, "colaboradores_id":venda.id_colaborador, "nota_fiscal":venda.nota_fiscal}) # Executando a query
            conexao.commit() # Commitando o cadastro
        return "Venda cadastrada."

    def teste_read(self, id):
        '''Recebe o ID de uma venda e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM vendas WHERE id = :id""") # query
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            venda_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).all() # É retornada uma lista com uma tupla dentro
        venda_bd = venda_bd[0] # Pega a tupla da lista

        if venda_bd: # Caso o venda exista
            venda = Venda(venda_bd[1], venda_bd[2], venda_bd[3], venda_bd[4], venda_bd[0]) # Transformando venda em um objeto
            return venda # venda é retornado
        return None # Caso não, None é retornado
    
    def teste_update(self, id, clientes_id_atributo, atributo_update):
        '''Recebe o ID de um venda, o clientes_id do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        query = text (f'''UPDATE vendas
                    SET {clientes_id_atributo} = {atributo_update}
                    WHERE id = {id}''')
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão
            conexao.execute (query)
            conexao.commit()
            
        return "Atributo atualizado."