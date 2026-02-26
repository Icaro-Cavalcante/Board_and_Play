from sqlalchemy import text
from ..modules.domain.produtos import Produto

class Repository_produto():
    '''Classe que realiza as operações do banco de dados relacionadas a produto.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, produto):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text ("""INSERT OR IGNORE INTO produtos
            (id, codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria)
            VALUES (:id, :codigo_barras, :nome, :custo_aquisicao, :data_aquisicao, :categoria)
            """), {"id":produto.id, "codigo_barras":produto.codigo_barras, "nome":produto.nome, "custo_aquisicao":produto.custo_aquisicao, "data_aquisicao":produto.data_aquisicao, "categoria":produto.categoria} # Query
            )
            conexao.commit() # Commitando o cadastro
        print("Jogo cadastrado.")

    def read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            produto_bd = conexao.execute (text ("""SELECT * FROM produtos WHERE id = ?"""), (id, ) # query
            ).first() 

        if produto_bd: # Caso o produto exista
            produto = Produto(produto_bd[0], produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[4], produto_bd[5]) # Transformando produto em um objeto
            return produto # Produto é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text (f'''UPDATE produto
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        print("Atributo atualizado.")

# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def create(self, produto):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text ("""INSERT OR IGNORE INTO produtos
            (id, codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria)
            VALUES (:id, :codigo_barras, :nome, :custo_aquisicao, :data_aquisicao, :categoria)
            """), {"id":produto.id, "codigo_barras":produto.codigo_barras, "nome":produto.nome, "custo_aquisicao":produto.custo_aquisicao, "data_aquisicao":produto.data_aquisicao, "categoria":produto.categoria} # Query
            )
            conexao.commit() # Commitando o cadastro
        return "Jogo cadastrado."

    def read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            produto_bd = conexao.execute (text ("""SELECT * FROM produtos WHERE id = ?"""), (id, ) # query
            ).first() 

        if produto_bd: # Caso o produto exista
            produto = Produto(produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[4], produto_bd[5], produto_bd[0]) # Transformando produto em um objeto
            return produto # Produto é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text (f'''UPDATE produto
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        return "Atributo atualizado."