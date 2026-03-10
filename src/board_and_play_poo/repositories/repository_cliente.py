from sqlalchemy import text
from src.board_and_play_poo.modules.domain.clientes import Cliente

class RepositoryCliente():
    '''Classe que realiza as operações do banco de dados relacionadas a cliente'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, cliente):
        '''Recebe um objeto de cliente e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO clientes
            (cpf, nome, email, contato, status)
            VALUES (:cpf, :nome, :email, :contato, :status)""") # Query

            conexao.execute (query, {"cpf":cliente.cpf, "nome":cliente.nome, "email":cliente.email, "contato":cliente.contato, "status":cliente.status} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return "Cliente cadastrado"
        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de um cliente e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM clientes WHERE id = :id""")
            cliente = conexao.execute (query, {"id": id, } # query
            ).first()
            conexao.close()
            if cliente:
                return Cliente(cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[0])
        return None # Caso não, None é retornado
    
    def imprimir_dados(self, tupla):
        '''Imprime dados de uma tupla de cliente, semelhante a uma função __str__'''
        dic_atributos = {1: "ID", 2: "CPF", 3: "Nome", 4: "Email", 5: "Contato", 6: "Status"}
        atributo_num = 1
        for atributo in tupla:
            print(f"{dic_atributos[atributo_num]}: {atributo}")
            atributo_num += 1
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um cliente, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE clientes
                    SET {nome_atributo} = :atributo_update
                    WHERE id = :id''') # query
            conexao.execute (query, {"atributo_update": atributo_update, "id": id})
            conexao.commit()
            conexao.close()
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"
        
    def inactivate(self, id):
        '''Recebe o ID de um cliente e altera seus status para inativo no banco de dados'''
         # query
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE clientes
                    SET status = :inativar
                    WHERE id = :id''')
            conexao.execute (query, {"inativar": "INATIVADO", "id": id})
            conexao.commit()
            conexao.close()
            return "Cliente inativado"
        else:
            return "Não foi possível conectar"
