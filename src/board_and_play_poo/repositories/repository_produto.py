from sqlalchemy import text
from src.board_and_play_poo.modules.domain.produtos import Produto

class Repository_produto():
    '''Classe que realiza as operações do banco de dados relacionadas a produto.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
        
    def create(self, produto):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados do ambiente.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO produtos
                (codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria, quantidade)
                VALUES (:codigo_barras, :nome, :custo_aquisicao, :data_aquisicao, :categoria, :quantidade)
                """) # Query
            # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (query , {"codigo_barras":produto.codigo_barras, "nome":produto.nome, "custo_aquisicao":produto.custo_aquisicao, "data_aquisicao":produto.data_aquisicao, "categoria":produto.categoria, "quantidade":produto.quantidade},  # Executa a query, passa o dicionário e cadastra um novo produto
            )
            conexao.commit() # Commitando o cadastro
            return("Jogo cadastrado.")
        else: # Se a conexão não existir
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        conexao = self.database.conectar()  # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""SELECT * FROM produtos WHERE id = :id""") # query
            produto_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).all() # É retornada uma lista com uma tupla dentro
            produto_bd = produto_bd[0] # Pega a tupla da lista

            if produto_bd: # Caso o produto exista
                produto = Produto(produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[4], produto_bd[5], produto_bd[6], produto_bd[0]) # Transformando produto em um objeto
                return produto # Produto é retornado
            return None # Caso não, None é retornado
        else: # Se a conexão não existir
            return "Não foi possível conectar"
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado.'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text (f'''UPDATE produtos
                        SET {nome_atributo} = :atributo_update
                        WHERE id = :id''') # query
            conexao.execute ((query), {"atributo_update": atributo_update, "id": id,}) # Exeutando a query e passando os parametros
            conexao.commit() # Commitando o update
            return "Atributo atualizado."
        else: # Se a conexão não existir
            return "Não foi possível conectar" 