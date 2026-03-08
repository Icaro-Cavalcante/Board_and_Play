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
            (comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao)
            VALUES (:comprovante, :data_hora, :valor_total, :forma_pagamento, :tipo_transacao) RETURNING id
            """)
            UtilId = conexao.execute (query, {"comprovante": transacao.comprovante,"data_hora": transacao.data_hora, "valor_total":transacao.valor_total, "forma_pagamento":transacao.forma_pagamento, "tipo_transacao":transacao.tipo_transacao} # Executa a query, passa o dicionário (a variável query) e cadastra uma nova transação
            )
            conexao.commit() # Commitando o cadastro
            return UtilId
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
            return transacao # transação é retornada
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de uma transação, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f'''UPDATE transacoes
                    SET {nome_atributo} = {atributo_update}
                    WHERE id = {id}''')
            conexao.execute (query) # Executando a query
            conexao.commit() # Commitando o update
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"