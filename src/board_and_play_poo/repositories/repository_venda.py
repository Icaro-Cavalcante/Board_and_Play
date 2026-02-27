from sqlalchemy import text
from ..modules.domain.venda import Venda

class Repository_venda():
    '''Classe que realiza as operações do banco de dados relacionadas a venda.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, venda):
        '''Recebe um objeto de venda e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text ("""INSERT OR IGNORE INTO vendas
            (id, transacao_id, clientes_id, colaboradores_id, nota_fiscal)
            VALUES (:id, :transacao_id, :clientes_id, :colaboradores_id, :nota_fiscal)
            """), {"id":venda.id, "transacao_id":venda.transacao_id, "clientes_id":venda.clientes_id, "colaboradores_id":venda.colaboradores_id, "nota_fiscal":venda.nota_fiscal} # Query
            )
            conexao.commit() # Commitando o cadastro
        print("Jogo cadastrado.")

    def read(self, id):
        '''Recebe o ID de uma venda e retorna um objeto dos seus dados'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            venda_bd = conexao.execute (text ("""SELECT * FROM vendas WHERE id = ?"""), (id, ) # query
            ).first() 

        if venda_bd: # Caso o venda exista
            venda = Venda(venda_bd[0], venda_bd[1], venda_bd[2], venda_bd[3], venda_bd[4]) # Transformando venda em um objeto
            return venda # venda é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, clientes_id_atributo, atributo_update):
        '''Recebe o ID de um venda, o clientes_id do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text (f'''UPDATE venda
                    SET {clientes_id_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        print("Atributo atualizado.")

# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, venda):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text ("""INSERT OR IGNORE INTO vendas
            (id, transacao_id, clientes_id, colaboradores_id, nota_fiscal)
            VALUES (:id, :transacao_id, :clientes_id, :colaboradores_id, :nota_fiscal)
            """), {"id":venda.id, "transacao_id":venda.transacao_id, "clientes_id":venda.clientes_id, "colaboradores_id":venda.colaboradores_id, "nota_fiscal":venda.nota_fiscal} # Query
            )
            conexao.commit() # Commitando o cadastro
        return "Jogo cadastrado."

    def teste_read(self, id):
        '''Recebe o ID de um venda e retorna um objeto dos seus dados'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            venda_bd = conexao.execute (text ("""SELECT * FROM vendas WHERE id = ?"""), (id, ) # query
            ).first() 

        if venda_bd: # Caso o venda exista
            venda = Venda(venda_bd[0], venda_bd[1], venda_bd[2], venda_bd[3], venda_bd[4]) # Transformando venda em um objeto
            return venda # venda é retornado
        return None # Caso não, None é retornado
    
    def teste_update(self, id, clientes_id_atributo, atributo_update):
        '''Recebe o ID de um venda, o clientes_id do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text (f'''UPDATE venda
                    SET {clientes_id_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        return "Atributo atualizado."