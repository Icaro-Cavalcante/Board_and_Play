from sqlalchemy import text

class Repository_produto():
    '''Classe que realiza as operações do banco de dados relacionadas a produto.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
        
# ------------------------------------------------------ CRUD ------------------------------------------------------

    def create(self, tupla):
        '''Recebe uma tupla com os parâmetros de atributos da generalização Produto para suas especificações'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO produtos
                (nome, codigo_barras, categoria)
                VALUES (:nome, :codigo_barras, :categoria) RETURNING id
                """) # Query
            # Estabelecendo a conexão com o banco de dados de testes
            result = conexao.execute (query , {"nome":tupla[0], "codigo_barras":tupla[1], "categoria":tupla[2]},  # Executa a query, passa o dicionário e cadastra um novo produto
            )
            obj_id = result.fetchone()[0]
            conexao.commit() # Commitando o cadastro
            return(obj_id)
        else: # Se a conexão não existir
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um produto e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar()  # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""SELECT * FROM produtos WHERE id = :id""") # query
            produto_bd = conexao.execute (query, {"id": id, } # Executa a query, passa o id e recebe os dados
            ).first() # É retornada uma lista com uma tupla dentro
            return produto_bd # Produto é retornado
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

    def delete(self):
        '''Por regra de negócio, nenhum produto será deletado do banco de dados, apenas terá seu status atualizado para inativo.'''
        pass