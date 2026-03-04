from sqlalchemy import text
from src.board_and_play_poo.modules.domain.jogos import Jogo

class Repository_jogo():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, jogo):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO jogos
            (produto_id, genero, descricao, idade_min, num_jogadores)
            VALUES (:produto_id, :genero, :descricao, :idade_min, :num_jogadores)""") # Query

            conexao.execute (query, {"produto_id":jogo.produto_id, "genero":jogo.genero, "descricao":jogo.descricao, "idade_min":jogo.idade_min, "num_jogadores":jogo.num_jogadores} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "Jogo cadastrado"

        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um jogo e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM jogos WHERE id = :id""")
            jogo = conexao.execute (query, {"id": id, } # query
            ).first()
            return jogo # Jogo é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado.'''
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