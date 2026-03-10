from sqlalchemy import text
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo
from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto

class RepositoryJogoVenda():
    '''Classe que realiza as operações do banco de dados relacionadas a jogo venda'''
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.produto_repo = RepositoryProduto(self.database, self.table)
        self.jogo_repo = RepositoryJogo(self.database, self.table)

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, jogo_venda):
        '''Recebe um objeto de jogo venda e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO jogos_venda
            (jogo_id, quantidade)
            VALUES (:jogo_id, :quantidade)""") # Query

            conexao.execute (query, {"jogo_id":jogo_venda.jogo_id, "quantidade": jogo_venda.quantidade} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return "Jogo venda cadastrado"
        else: # Se não
            return "Não foi possível conectar"

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
            conexao.close()
            return tupla
        conexao.close()
        return None # Caso não, None é retornado

    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um jogo_venda, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado'''
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
                    return self.produto_repo.update(id_produto, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo:
                    return self.jogo_repo.update(id_jogo, nome_atributo, atributo_update)
                elif nome_atributo in atributos_jogo_venda:
                    query = text (f'''UPDATE jogos_venda
                            SET {nome_atributo} = :atributo_update
                            WHERE id = :id''') # query
                    conexao.execute (query, {"atributo_update": atributo_update, "id": id})
                    conexao.commit()
                    conexao.close()
                    return "Atributo atualizado."
                else:
                    conexao.close()
                    return "Atributo inválido"
            else:
                conexao.close()
                return "Jogo venda não existe"
        else:
            conexao.close()
            return "Não foi possível conectar"
