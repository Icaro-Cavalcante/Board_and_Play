from sqlalchemy import text
from src.board_and_play_poo.modules.domain.produtos import Produto

class Repository_produto():
    '''Classe que realiza as operações do banco de dados relacionadas a produto.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, produto):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados.'''
        query = text ("""INSERT OR IGNORE INTO produtos
            (codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria, quantidade)
            VALUES (:codigo_barras, :nome, :custo_aquisicao, :data_aquisicao, :categoria, :quantidade)""") # Query
        
        with self.database.conectar() as conexao: # Estabelecendo a conexão com o banco de dados
            conexao.execute (query , {"codigo_barras":produto.codigo_barras, "nome":produto.nome, "custo_aquisicao":produto.custo_aquisicao, "data_aquisicao":produto.data_aquisicao, "categoria":produto.categoria, "quantidade": produto.quantidade} # Executa a query, passa o dicionário e cadastra um novo produto
            )
            conexao.commit() # Commitando o cadastro
        return "Jogo cadastrado."

    def read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM produtos WHERE id = :id""") # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão com o banco de dados
            produto_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).all() # É retornada uma lista com uma tupla dentro
        produto_bd = produto_bd[0] # Pega a tupla da lista

        if produto_bd: # Caso o produto exista
            produto = Produto(produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[4], produto_bd[5], produto_bd[6], produto_bd[0]) # Transformando produto em um objeto
            return produto # Produto é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        query = text (f'''UPDATE produtos
                    SET {nome_atributo} = {atributo_update}
                    WHERE id = {id}''') # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão com o banco de dados
            conexao.execute (query) # Exeutando a query
            conexao.commit() # Commitando o update
            
        print("Atributo atualizado.")

# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, produto):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados de testes.'''
        query = text ("""INSERT OR IGNORE INTO produtos
            (codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria, quantidade)
            VALUES (:codigo_barras, :nome, :custo_aquisicao, :data_aquisicao, :categoria, :quantidade)
            """) # Query
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (query , {"codigo_barras":produto.codigo_barras, "nome":produto.nome, "custo_aquisicao":produto.custo_aquisicao, "data_aquisicao":produto.data_aquisicao, "categoria":produto.categoria, "quantidade":produto.quantidade} # Executa a query, passa o dicionário e cadastra um novo produto
            )
            conexao.commit() # Commitando o cadastro
        return "Jogo cadastrado."

    def teste_read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM produtos WHERE id = :id""") # query
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            produto_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).all() # É retornada uma lista com uma tupla dentro
        produto_bd = produto_bd[0] # Pega a tupla da lista

        if produto_bd: # Caso o produto exista
            produto = Produto(produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[4], produto_bd[5], produto_bd[6], produto_bd[0]) # Transformando produto em um objeto
            return produto # Produto é retornado
        return None # Caso não, None é retornado
    
    def teste_update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados de testes.'''
        query = text (f'''UPDATE produtos
                    SET {nome_atributo} = {atributo_update}
                    WHERE id = {id}''') # query
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (query) # Exeutando a query
            conexao.commit() # Commitando o update
            
        return "Atributo atualizado."