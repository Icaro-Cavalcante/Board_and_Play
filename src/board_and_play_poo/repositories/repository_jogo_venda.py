from sqlalchemy import text
from src.board_and_play_poo.modules.domain.jogos_venda import Jogo_venda
from src.board_and_play_poo.repositories.repository_jogo import Repository_jogo
from src.board_and_play_poo.repositories.repository_produto import Repository_produto
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
jogo_repo = Repository_jogo(db, tb)
produto_repo = Repository_produto(db, tb)

class Repository_jogo_venda():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo venda.'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

    def create(self, jogo_venda):
        '''Recebe uma tupla de jogo venda e cadastra ele no banco de dados.'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO jogos_venda
            (jogo_id, quantidade)
            VALUES (:jogo_id, :quantidade)""") # Query

            conexao.execute (query, {"jogo_id":jogo_venda[0], "quantidade": jogo_venda[1]} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            return "Jogo venda cadastrado"
        else: # Se não
            return("Não foi possível conectar")

    def read(self, id):
        '''Recebe o ID de um jogo venda e retorna um objeto dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""
            SELECT produtos.nome, produtos.codigo_barras, produtos.categoria, jogos.genero, jogos.descricao, jogos.idade_min, jogos.num_jogadores, jogos_venda.quantidade, jogos.produto_id, jogos_venda.jogo_id, jogos_venda.id
            FROM jogos_venda
            INNER JOIN jogos ON jogos_venda.jogo_id = jogos.id
            INNER JOIN produtos ON jogos.produto_id = produtos.id
            WHERE jogos_venda.id = :id""")
            tupla = conexao.execute (query, {"id": id, } # query
            ).first()
            if tupla:
                jogo_venda = Jogo_venda(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10])
                return jogo_venda # Jogo venda é retornado
        return None # Caso não, None é retornado

    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo_venda, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado.'''
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            atributos_produto = ["nome", "codigo_barras", "categoria"]
            atributos_jogo = ["genero", "descricao", "idade_min", "num_jogadores"]
            atributos_jogo_venda = ["quantidade"]

            jogo_venda = self.read(id)
            if jogo_venda:
                id_jogo = jogo_venda.jogo_id
                id_produto = jogo_venda.produto_id
                if nome_atributo in atributos_produto:
                    return produto_repo.update(id_produto, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo:
                    return jogo_repo.update(id_jogo, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo_venda:
                    query = text (f'''UPDATE jogos_venda
                            SET {nome_atributo} = :atributo_update
                            WHERE id = :id''') # query
                    conexao.execute (query, {"atributo_update": atributo_update, "id": id})
                    conexao.commit()
                    return "Atributo atualizado."
                else:
                    return "Atributo inválido"
            else:
                return "Jogo venda não existe"
        else:
            return "Não foi possível conectar"
