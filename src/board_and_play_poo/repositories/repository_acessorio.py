from sqlalchemy import text

class RepositoryAcessorio():
    '''Classe que realiza as operações do banco de dados relacionadas a acessorio'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, acessorio):
        '''Recebe um objeto de acessorio e cadastra ele no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO acessorios
            (produto_id, tipo_acessorio, quantidade)
            VALUES (:produto_id, :tipo_acessorio, :quantidade)""") # Query

            conexao.execute (query, {"produto_id":acessorio.produto_id, "tipo_acessorio":acessorio.tipo_acessorio, "quantidade":acessorio.quantidade} # Executando a query
            )
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return "Acessório cadastrado"
        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de um acessorio e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM acessorios WHERE id = :id""")
            acessorio = conexao.execute (query, {"id": id, } # query
            ).first()
            return acessorio # Acessório é retornado
        return None # Caso não, None é retornado
    
    def imprimir_dados(self, tupla):
        '''Imprime dados de uma tupla de acessório, semelhante a uma função __str__'''
        dic_atributos = {1: "Nome", 2: "Código de barras", 3: "Categoria do Produto", 4: "Tipo do acessório", 5: "Quantidade", 6: "ID de produto", 7: "ID de acessório"}
        atributo_num = 1
        for atributo in tupla:
            print(f"{dic_atributos[atributo_num]}: {atributo}")
            atributo_num += 1

    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um acessorio, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE acessorios
                    SET {nome_atributo} = :atributo_update
                    WHERE id = :id''') # query
            conexao.execute (query, {"atributo_update": atributo_update, "id": id})
            conexao.commit()
            conexao.close()
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"
