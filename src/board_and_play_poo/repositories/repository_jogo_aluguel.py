from sqlalchemy import text
from src.board_and_play_poo.modules.domain.jogo_aluguel import Jogo_aluguel
from src.board_and_play_poo.repositories.repository_jogo import Repository_jogo
from src.board_and_play_poo.repositories.repository_produto import Repository_produto
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
jogo_repo = Repository_jogo(db, tb)
produto_repo = Repository_produto(db, tb)

class Repository_jogo_aluguel():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo aluguel.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ------------------------------------------- CRUD -------------------------------------------

    def create(self, jogo_aluguel):
        '''Recebe um objeto de jogo aluguel e cadastra ele no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO jogos_aluguel
            (jogo_id, etiqueta, status)
            VALUES (:jogo_id, :etiqueta, :status)""") # Query

            conexao.execute (query, {"jogo_id":jogo_aluguel.jogo_id, "etiqueta":jogo_aluguel.etiqueta, "status":jogo_aluguel.status} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "Jogo aluguel cadastrado"

        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um jogo aluguel e retorna um objeto dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT produtos.nome, produtos.codigo_barras, produtos.categoria, jogos.genero, jogos.descricao, jogos.idade_min, jogos.num_jogadores, jogos_aluguel.etiqueta, jogos_aluguel.status, jogos.produto_id, jogos_aluguel.jogo_id, jogos_aluguel.id
            FROM jogos_aluguel
            INNER JOIN jogos ON jogos_aluguel.jogo_id = jogos.id
            INNER JOIN produtos ON jogos.produto_id = produtos.id
            WHERE jogos_aluguel.id = :id""")
            tupla = conexao.execute (query, {"id": id, } # query
            ).first()
            if tupla:
                jogo_aluguel = Jogo_aluguel(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11])
                return jogo_aluguel # Jogo aluguel é retornado
        return None # Caso não, None é retornado
    
    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo aluguel, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado.'''
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            atributos_produto = ["nome", "codigo_barras", "categoria"]
            atributos_jogo = ["genero", "descricao", "idade_min", "num_jogadores"]
            atributos_jogo_aluguel = ["etiqueta", "status"]

            jogo_aluguel = self.read(id)
            if jogo_aluguel:
                id_jogo = jogo_aluguel.jogo_id
                id_produto = jogo_aluguel.produto_id
                print(f"DEBUG: id_produto={id_produto}, id_jogo={id_jogo}")  # Debug
                if nome_atributo in atributos_produto:
                    return produto_repo.update(id_produto, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo:
                    return jogo_repo.update(id_jogo, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo_aluguel:
                    query = text (f'''UPDATE jogos_aluguel
                            SET {nome_atributo} = :atributo_update
                            WHERE id = :id''') # query
                    conexao.execute (query, {"atributo_update": atributo_update, "id": id})
                    conexao.commit()
                    return "Atributo atualizado."
                else:
                    return "Atributo inválido"
            else:
                return "Jogo aluguel não existe"
        else:
            return "Não foi possível conectar"

    def inactivate(self, id):
        '''Recebe o ID de um jogo aluguel e coloca o status como "INATIVO".'''
        query = text (f'''UPDATE jogos_aluguel
                    SET status = "INATIVO"
                    WHERE id = {id}''') # query
        with self.database.conectar() as conexao: # Estabelecendo a conexão com o banco de dados
            conexao.execute(query) # Executa a query
            conexao.commit() # Commitando a mudança
            return ("Jogo aluguel mudado para INATIVO com sucesso.")
