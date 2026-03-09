from sqlalchemy import text

class RepositoryJogo():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, jogo):
        '''Recebe uma tupla de jogo e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO jogos
            (produto_id, genero, descricao, idade_min, num_jogadores)
            VALUES (:produto_id, :genero, :descricao, :idade_min, :num_jogadores) RETURNING id
            """) # Query

            result = conexao.execute (query, {"produto_id":jogo[0], "genero":jogo[1], "descricao":jogo[2], "idade_min":jogo[3], "num_jogadores":jogo[4]} # Executando a query
            )
            obj_id = result.scalar()
            conexao.commit() # Commitando o cadastro
            return obj_id

        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de um jogo e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM jogos WHERE id = :id""")
            jogo = conexao.execute (query, {"id": id, } # query
            ).first()
            return jogo # Jogo é retornado
        return None # Caso não, None é retornado
    
    def find(self, produto_id):
        '''Recebe o ID de um produto e retorna a tupla com os dados do jogo agregado ao id'''
        conexao = self.database.conectar()
        if conexao: 
            query = text(f"""SELECT * FROM jogos WHERE produto_id = :id""")
            jogo = conexao.execute (query, {"id": produto_id, }
            ).first()
            return jogo
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE jogos
                    SET {nome_atributo} = :atributo_update
                    WHERE id = :id''') # query
            conexao.execute (query, {"atributo_update": atributo_update, "id": id})
            conexao.commit()
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"