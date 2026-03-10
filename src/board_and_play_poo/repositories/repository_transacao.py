from sqlalchemy import text
from ..modules.domain.transacoes import Transacao

class RepositoryTransacao():
    '''Classe que realiza as operações do banco de dados relacionadas a transacao'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, transacao):
        conexao = self.database.conectar()
        if conexao: # Estabelecendo a conexão
            query = text ("""INSERT OR IGNORE INTO transacoes
            (id, comprovante, valor_total, forma_pagamento, tipo_transacao)
            VALUES (:id, :comprovante, :valor_total, :forma_pagamento, :tipo_transacao)
            """)
            result = conexao.execute (query, {"id": 1, "comprovante": transacao[0], "valor_total":transacao[1], "forma_pagamento":transacao[2], "tipo_transacao":transacao[3]}
            ) # Executa a query, passa o dicionário (a variável query) e cadastra uma nova transação
            id = result.lastrowid
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return id
        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de uma transação e retorna um objeto dos seus dados'''
        conexao = self.database.conectar()
        if conexao: # Estabelecendo a conexão
            query = text ("""SELECT * FROM transacoes WHERE id = :id""")
            transacoes_bd = conexao.execute (query, {"id": id} # query
            ).all() # É retornada uma lista com uma tupla dentro
        transacoes_bd = transacoes_bd[0] # Pega a tupla da lista

        if transacoes_bd: # Caso a transação exista
            transacao = Transacao(transacoes_bd[0], transacoes_bd[1], transacoes_bd[2], transacoes_bd[3], transacoes_bd[4], transacoes_bd[5]) # Transformando transação em um objeto
            conexao.close()
            return transacao # transação é retornada
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de uma transação, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f'''UPDATE transacoes
                    SET {nome_atributo} = :upd
                    WHERE id = :id''')
            conexao.execute(query, {"id": id, "upd": atributo_update}) # Executando a query
            conexao.commit() # Commitando o update
            conexao.close()
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"