from sqlalchemy import text
from ..modules.domain.jogos import Jogo

class Repository_jogo():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
# ------------------------------------------------- CRUD REAL --------------------------------------------------

    def create(self, jogo):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text ("""INSERT OR IGNORE INTO jogos
            (id, produto_id, etiqueta, genero, descricao, idade_min, num_jogadores, tipo_jogo, status)
            VALUES (:id, :produto_id, :etiqueta, :genero, :descricao, :idade_min, :num_jogadores, :tipo_jogo, :status)
            """), {"id":jogo.id, "produto_id":jogo.produto_id, "etiqueta":jogo.etiqueta, "genero":jogo.genero, "descricao":jogo.descricao, "idade_min":jogo.idade_min, "num_jogadores":jogo.num_jogadores, "tipo_jogo":jogo.tipo_jogo, "status":jogo.status} # Query
            )
            conexao.commit() # Commitando o cadastro
        print("Jogo cadastrado.")

    def read(self, id):
        '''Recebe o ID de um jogo e retorna um objeto dos seus dados'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            jogo_bd = conexao.execute (text ("""SELECT * FROM jogos WHERE id = ?"""), (id, ) # query
            ).first() 

        if jogo_bd: # Caso o jogo exista
            jogo = Jogo(jogo_bd[0], jogo_bd[1], jogo_bd[2], jogo_bd[3], jogo_bd[4], jogo_bd[5], jogo_bd[6], jogo_bd[7], jogo_bd[8]) # Transformando jogo em um objeto
            return jogo # Jogo é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados.'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text (f'''UPDATE jogos
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        print("Atributo atualizado.")

    def inactivate(self, id):
        '''Recebe o ID de um jogo e altera seus status para inativo no banco de dados'''
        with self.database.conectar() as conexao: # Estabelecendo a conexão
            conexao.execute (text (f'''UPDATE jogos
                    SET status = ?
                    WHERE id = ?''', ("inativo", id))
                )
            conexao.commit()
        print("Jogo inativado.")

# ------------------------------------------------- CRUD TESTES --------------------------------------------------

    def teste_create(self, jogo):
        '''Recebe um objeto de jogo e cadastra ele no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text ("""INSERT OR IGNORE INTO jogos
            (id, produto_id, etiqueta, genero, descricao, idade_min, num_jogadores, tipo_jogo, status)
            VALUES (:id, :produto_id, :etiqueta, :genero, :descricao, :idade_min, :num_jogadores, :tipo_jogo, :status)
            """), {"id":jogo.id, "produto_id":jogo.produto_id, "etiqueta":jogo.etiqueta, "genero":jogo.genero, "descricao":jogo.descricao, "idade_min":jogo.idade_min, "num_jogadores":jogo.num_jogadores, "tipo_jogo":jogo.tipo_jogo, "status":jogo.status} # Query
            )
            conexao.commit() # Commitando o cadastro
        return"Jogo cadastrado."

    def teste_read(self, id):
        '''Recebe o ID de um jogo e retorna um objeto dos seus dados'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            jogo_bd = conexao.execute (text ("""SELECT * FROM jogos WHERE id = ?"""), (id, ) # query
            ).first() 

        if jogo_bd: # Caso o jogo exista
            jogo = Jogo(jogo_bd[1], jogo_bd[2], jogo_bd[3], jogo_bd[4], jogo_bd[5], jogo_bd[6], jogo_bd[7], jogo_bd[8], jogo_bd[0]) # Transformando jogo em um objeto
            return jogo # Jogo é retornado
        return None # Caso não, None é retornado
    
    def teste_update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text (f'''UPDATE jogos
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id)) # query
                )
            conexao.commit()
            
        return"Atributo atualizado."

    def teste_inactivate(self, id):
        '''Recebe o ID de um jogo e altera seus status para inativo no banco de dados de testes.'''
        with self.database.conectar_test() as conexao: # Estabelecendo a conexão com o banco de dados de testes
            conexao.execute (text (f'''UPDATE jogos
                    SET status = ?
                    WHERE id = ?''', ("inativo", id))
                )
            conexao.commit()
        return"Jogo inativado."