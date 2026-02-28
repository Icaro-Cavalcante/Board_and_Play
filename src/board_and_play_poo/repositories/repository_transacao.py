from sqlalchemy import text
from datetime import datetime
from ..modules.domain.transacoes import Transacao

class Repository_transacao():
    '''Classe que realiza as operações do banco de dados relacionadas a transacao.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, transacao):
        '''Recebe um objeto de transação e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            query = text ("""INSERT OR IGNORE INTO transacoes
            (valor_total, forma_pagamento, status_pagamento, tipo_transacao)
            VALUES (:valor_total, :forma_pagamento, :status_pagamento, :tipo_transacao)
            """)
            conexao.execute (query, {"valor_total":transacao.valor_total, "forma_pagamento":transacao.forma_pagamento, "status_pagamento":transacao.status_pagamento, "tipo_transacao":transacao.tipo_transacao} # Executa a query, passa o dicionário (a variável query) e cadastra uma nova transação
            )
            conexao.commit() # Commitando o cadastro
        print("Transação cadastrada.")

    def read(self, id):
        '''Recebe o ID de uma transação e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM transacoes WHERE id = :id""")
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            transacoes_bd = conexao.execute (query, {"id": id} # query
            ).all() # É retornada uma lista com uma tupla dentro
        transacoes_bd = transacoes_bd[0] # Pega a tupla da lista

        if transacoes_bd: # Caso a transação exista
            transacao = Transacao(transacoes_bd[0], transacoes_bd[1], transacoes_bd[2], transacoes_bd[3], transacoes_bd[4], transacoes_bd[5]) # Transformando transação em um objeto
            return transacao # transação é retornada
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de uma transação, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        query = text (f'''UPDATE transacoes
                    SET {nome_atributo} = {atributo_update}
                    WHERE id = {id}''')
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (query) # Executando a query
            conexao.commit() # Commitando o update
            
        print("Atributo atualizado.")

    def inactivate(self, id):
        '''Reccebe o ID de uma transação e coloca o status de pagamento como "INATIVA".'''
        query = text (f'''UPDATE transacoes
                    SET status_pagamento = "INATIVA"
                    WHERE id = {id}''') # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão com o banco de dados
            conexao.execute(query) # Executa a query
            conexao.commit() # Commitando a mudança
            print("Transação mudada para INATIVA com sucesso.")

    def pagar(self, id):
        '''Recebe o ID de uma transação e coloca o status de pagamento como "PAGO".'''
        query = text(f'''UPDATE transacoes
                    SET status_pagamento = "PAGO"
                    WHERE id = {id}''') # query
        with self.database.conectar() as conexao:
            conexao.execute(query) # Executa a query (atualiza para pago)
            conexao.commit # Commita a mudança
            print("Pasagamento registrado com sucesso.")
# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, transacao):
        '''Recebe um objeto de transação e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            query = text ("""INSERT OR IGNORE INTO transacoes
            (data_hora, valor_total, forma_pagamento, status_pagamento, tipo_transacao)
            VALUES (:data_hora, :valor_total, :forma_pagamento, :status_pagamento, :tipo_transacao)""")

            conexao.execute (query, {"data_hora":datetime.now(), "valor_total":transacao.valor_total, "forma_pagamento":transacao.forma_pagamento, "status_pagamento":transacao.status_pagamento, "tipo_transacao":transacao.tipo_transacao} # Query
            )
            conexao.commit() # Commitando o cadastro
        return "Transação cadastrada."

    def teste_read(self, id):
        '''Recebe o ID de uma transação e retorna um objeto dos seus dados'''
        query = text ("""SELECT * FROM transacoes WHERE id = :id""")
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão
            transacoes_bd = conexao.execute (query, {"id": id} # query
            ).all() # É retornada uma lista com uma tupla dentro
        transacoes_bd = transacoes_bd[0] # Pega a tupla da lista

        if transacoes_bd: # Caso a transação exista
            transacao = Transacao(transacoes_bd[1], transacoes_bd[2], transacoes_bd[3], transacoes_bd[4], transacoes_bd[5], transacoes_bd[0]) # Transformando transação em um objeto
            return transacao # transação é retornada
        return None # Caso não, None é retornado
    
    def teste_update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de uma transação, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        query = text (f'''UPDATE transacoes
                    SET {nome_atributo} = {atributo_update}
                    WHERE id = {id}''')
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão
            conexao.execute (query) # Executando a query
            conexao.commit() # Commitando o update

        return "Atributo atualizado."
    
    def teste_inactivate(self, id):
        '''Reccebe o ID de uma transação e coloca o status de pagamento como "INATIVA".'''
        query = text (f'''UPDATE transacoes
                    SET status_pagamento = "INATIVA"
                    WHERE id = {id}''')
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute(query) # Executa a query
            conexao.commit() # Commitando a mudança

            return "Transação mudada para INATIVA com sucesso."

    def teste_pagar(self, id):
        '''Recebe o ID de uma transação e coloca o status de pagamento como "PAGO".'''
        query = text(f'''UPDATE transacoes
                    SET status_pagamento = "PAGO"
                    WHERE id = {id}''') # query
        with self.database.conectar_test() as conexao:
            conexao.execute(query) # Executa a query (atualiza para pago)
            conexao.commit # Commita a mudança
            return"Pasagamento registrado com sucesso."