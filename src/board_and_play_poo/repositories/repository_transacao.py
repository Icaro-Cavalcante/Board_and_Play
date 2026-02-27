from sqlalchemy import text
from ..modules.domain.transacoes import Transacao

class Repository_transacao():
    '''Classe que realiza as operações do banco de dados relacionadas a transacao.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, transacao):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text ("""INSERT OR IGNORE INTO transacoes
            (id, data_hora, valor_total, forma_pagamento, status_pagamento, tipo_transacao)
            VALUES (:id, :data_hora, :valor_total, :forma_pagamento, :status_pagamento, :tipo_transacao)
            """), {"id":transacao.id, "data_hora":transacao.data_hora, "valor_total":transacao.valor_total, "forma_pagamento":transacao.forma_pagamento, "status_pagamento":transacao.status_pagamento, "tipo_transacao":transacao.tipo_transacao} # Query
            )
            conexao.commit() # Commitando o cadastro
        print("Jogo cadastrado.")

    def read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            transacoes_bd = conexao.execute (text ("""SELECT * FROM transacoes WHERE id = ?"""), (id, ) # query
            ).first() 

        if transacoes_bd: # Caso o produto exista
            transacao = Transacao(transacoes_bd[0], transacoes_bd[1], transacoes_bd[2], transacoes_bd[3], transacoes_bd[4], transacoes_bd[5]) # Transformando produto em um objeto
            return transacao # Produto é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text (f'''UPDATE transacao
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        print("Atributo atualizado.")

    def inactivate(self, id):
        with self.database.conectar() as conexao:
            conexao.execute(text (f'''UPDATE transacao
                    SET status_pagamento = ?
                    WHERE id = ?''', ("INATIVA", id))
                    )
            conexao.commit()

    def pagar(self, id):
        with self.database.conectar() as conexao:
            conexao.execute(text('''UPDATE transacao
                    SET status_pagamento = ?
                    WHERE id = ?''', ("PAGO", id)))
            conexao.commit
# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, transacao):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text ("""INSERT OR IGNORE INTO transacoes
            (id, data_hora, valor_total, forma_pagamento, status_pagamento, tipo_transacao)
            VALUES (:id, :data_hora, :valor_total, :forma_pagamento, :status_pagamento, :tipo_transacao)
            """), {"id":transacao.id, "data_hora":transacao.data_hora, "valor_total":transacao.valor_total, "forma_pagamento":transacao.forma_pagamento, "status_pagamento":transacao.status_pagamento, "tipo_transacao":transacao.tipo_transacao} # Query
            )
            conexao.commit() # Commitando o cadastro
        return "Jogo cadastrado."

    def teste_read(self, id):
        '''Recebe o ID de um produto e retorna um objeto dos seus dados'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            transacoes_bd = conexao.execute (text ("""SELECT * FROM transacoes WHERE id = ?"""), (id, ) # query
            ).first() 

        if transacoes_bd: # Caso o produto exista
            transacao = Transacao(transacoes_bd[0], transacoes_bd[1], transacoes_bd[2], transacoes_bd[3], transacoes_bd[4], transacoes_bd[5]) # Transformando produto em um objeto
            return transacao # Produto é retornado
        return None # Caso não, None é retornado
    
    def teste_update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um produto, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text (f'''UPDATE transacao
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        return "Atributo atualizado."
    
    def teste_inactivate(self, id):
        with self.database.conectar_test() as conexao:
            conexao.execute(text (f'''UPDATE transacao
                    SET status_pagamento = ?
                    WHERE id = ?''', ("INATIVA", id))
                    )
            conexao.commit()

    def teste_pagar(self, id):
        with self.database.conectar_test() as conexao:
            conexao.execute(text('''UPDATE transacao
                    SET status_pagamento = ?
                    WHERE id = ?''', ("PAGO", id)))
            conexao.commit