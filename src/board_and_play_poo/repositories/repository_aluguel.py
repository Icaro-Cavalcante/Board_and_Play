from sqlalchemy import text
from src.board_and_play_poo.modules.domain.alugueis import Aluguel

class RepositoryAluguel():
    '''Classe que realiza as operações do banco de dados relacionadas a alugueis'''
    def __init__(self, database, table):
        self.database = database
        self.table = table

# ----------------------------------------------------------- CRUD -----------------------------------------------------------

    def create(self, aluguel):
        '''Recebe um objeto de aluguel e cadastra ela no banco de dados'''
        conexao = self.database.conectar() # Estabelecendo conexão com o banco de dados
        if conexao: # Se a conexão existir
            query = text ("""INSERT OR IGNORE INTO alugueis
            (transacao_id, cliente_id, colaborador_id, numero_contrato, data_inicio, data_prevista_devolucao, data_devolucao_real, status)
            VALUES (:transacao_id, :cliente_id, :colaborador_id, :numero_contrato, :data_inicio, :data_prevista_devolucao, :data_devolucao_real, :status)""") # Query

            aux = conexao.execute (query, {"transacao_id":aluguel.transacao_id, "cliente_id":aluguel.cliente_id, "colaborador_id":aluguel.colaborador_id, "numero_contrato":aluguel.numero_contrato, "data_inicio":aluguel.data_inicio, "data_prevista_devolucao":aluguel.data_prevista_devolucao, "data_devolucao_real":aluguel.data_devolucao_real, "status":aluguel.status} # Executando a query
            )
            id = aux.lastrowid
            conexao.commit() # Commitando o cadastro
            conexao.close()
            return id
        else: # Se não
            return "Não foi possível conectar"

    def read(self, id):
        '''Recebe o ID de um aluguel e retorna uma tupla dos seus dados'''
        conexao = self.database.conectar() # Estabelecendo a conexão
        if conexao: 
            query = text (f"""SELECT * FROM alugueis WHERE id = :id""")
            tupla = conexao.execute (query, {"id": id, } # query
            ).first()
            if tupla: # Se a tupla existir
                # Criando um objeto
                aluguel = self.tupla_objeto(tupla)
                return aluguel # Aluguel é retornado
            else:
                return None
        else:
            return None # Caso não, None é retornado
        
    def read_especifico(self, status):
        conexao = self.database.conectar()
        if conexao:
            query = text(f"""SELECT * FROM alugueis WHERE status = :status""")
            tupla = conexao.execute (query, {"status": status,}).all()
            if tupla:
                for tuple in tupla:
                    lista = []
                    aux = self.tupla_objeto(tuple)
                    lista.append(aux)
                return lista
            else:
                return None
    
    def tupla_objeto(self, tupla):
        return Aluguel(tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[3], tupla[2], tupla[1], tupla[0])

    def update(self, id, nome_atributo, atributo_update):
        '''Recebe o ID de um aluguel, o nome do atributo e o atributo atualizado e atualiza o atributo no banco de dados do ambiente selecionado'''
        # Nota 1: nome_atributo deve ser passado a partir de um dicionario. Exemplo dic = {1: "nome"}... nome deve ser passado como parâmetro e o usuário não pode passar nada que esteja fora dos atributos do dicionário.
        # Nota 2: nome_atributo não pode ser usado como um placeholder (:nome_atributo). Se for usado como um da erro
        conexao = self.database.conectar() # Estabelecendo a conexão com o banco de dados de testes
        if conexao:
            query = text (f'''UPDATE alugueis
                    SET {nome_atributo} = :atributo_update
                    WHERE id = :id''') # query
            conexao.execute (query, {"atributo_update": atributo_update, "id": id})
            conexao.commit()
            conexao.close()
            return "Atributo atualizado"
        else:
            return "Não foi possível conectar"
