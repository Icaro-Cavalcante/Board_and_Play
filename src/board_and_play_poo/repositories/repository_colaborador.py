from sqlalchemy import text
from src.board_and_play_poo.modules.domain.colaboradores import Colaborador

class Repository_colaborador():
    '''Classe que realiza as operações do banco de dados relacionadas a colaborador.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# --------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, colaborador):
        '''Recebe um objeto de colaborador e cadastra ele no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO colaboradores
            (cpf, nome, email, contato, contato_emergencia, salario, cargo, status)
            VALUES (:cpf, :nome, :email, :contato, :contato_emergencia, :salario, :cargo, :status)""") # Query

            conexao.execute (query, {"cpf":colaborador.cpf, "nome":colaborador.nome, "email":colaborador.email, "contato":colaborador.contato, "contato_emergencia":colaborador.contato_emergencia, "salario":colaborador.salario, "cargo":colaborador.cargo, "status":colaborador.status} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "Colaborador cadastrado"
        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um colaborador e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM colaboradores WHERE id = :id""")
            colaborador = conexao.execute (query, {"id": id, } # query
            ).first()
            return colaborador # Colaborador é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um colaborador, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado.'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE colaboradores
                    SET {nome_atributo} = :atributo_update
                    WHERE id = :id''') # query
            conexao.execute (query, {"atributo_update": atributo_update, "id": id})
            conexao.commit()
            return "Atributo atualizado"

    def inactivate(self, id):
        '''Recebe o ID de um colaborador e altera seus status para inativo no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE colaboradores
                    SET status = :inativar
                    WHERE id = :id''') # query
            conexao.execute (query, {"inativar": "INATIVADO", "id": id})
            conexao.commit()
        return "Colaborador inativado"