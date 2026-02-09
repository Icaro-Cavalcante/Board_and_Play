from pathlib import Path
from ..domain.alugaveis import Jogo_aluguel
import sqlite3
caminho_data = "src/board_and_play_poo/data/dados.db"

class Aluguel():
    def __init__(self, id_aluguel, id_jogo_aluguel, data_inicio, data_prevista_devolucao, multa_diaria, multa_avaria):
        self.id_aluguel = id_aluguel
        self.id_jogo_aluguel = id_jogo_aluguel
        self.data_inicio = data_inicio
        self.data_prevista_devolucao = data_prevista_devolucao
        self.multa_diaria = multa_diaria
        self.multa_avaria = multa_avaria

    def __str__(self):
        return f"ID do aluguel: {self.id_aluguel}\nID do jogo alugado: {self.id_jogo_aluguel}\nData de início: {self.data_inicio}\nData prevista para devolução: {self.data_prevista_devolucao}\nMulta diária: {self.multa_diaria}\nMulta de avaria: {self.multa_avaria}"
    
    def __eq__(self, outro):
        return self.id_aluguel == outro.id_aluguel
    
    def pasta_database():
        '''Método que cria a pasta (data) de dados, caso ela não exista'''
        caminho_diretorio = r"src/board_and_play_poo/data"
        caminho_diretorio = Path(caminho_diretorio)
        caminho_diretorio.mkdir(exist_ok=True)

    def tabela_aluguel():
        '''Cria a tabela de aluguéis no banco de dados'''
        Aluguel.pasta_database()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS aluguel 
                       (id_aluguel INTEGER UNIQUE, id_jogo_aluguel INTEGER, data_inicio TEXT, data_prevista_devolucao TEXT, multa_diaria REAL, multa_avaria REAL)''')

        cursor.close()
        conexao.close()

    def create():
        '''Recebe os atributos do aluguel e registra ele no banco de dados'''
        novo_id_aluguel = int(input("Informe o ID do aluguel: "))
        novo_id_jogo = int(input("Informe o ID do jogo alugado: "))
        nova_data_inicio = str(input("Informe a data de inicio do aluguel: "))
        nova_data_devolucao = str(input("Informe a data prevista de devolução do aluguel: "))
        nova_multa_diaria = str(input("Informe o valor da multa diária o do aluguel: "))
        nova_multa_avaria = str(input("Informe o valor da multa de avaria o do aluguel: "))

        novo_aluguel = Aluguel(novo_id_aluguel, novo_id_jogo, nova_data_inicio, nova_data_devolucao, nova_multa_diaria, nova_multa_avaria)

        Aluguel.tabela_aluguel()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''INSERT OR IGNORE INTO aluguel 
                       (id_aluguel, id_jogo_aluguel, data_inicio, data_prevista_devolucao, multa_diaria, multa_avaria)
                       VALUES (?, ?, ?, ?, ?, ?)''', (novo_aluguel.id_aluguel, novo_aluguel.id_jogo_aluguel, novo_aluguel.data_inicio, novo_aluguel.data_prevista_devolucao, novo_aluguel.multa_diaria, novo_aluguel.multa_avaria))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("\nAluguel criado.\n")

    def read(id):
        '''Recebe o id do aluguel e retorna uma tupla com os dados dele.'''
        Aluguel.tabela_aluguel()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM aluguel WHERE id_aluguel = ?''', (id))
        aluguel = cursor.fetchone()

        cursor.close()
        conexao.close()
        return aluguel

    def update(id, nome_atributo, atributo_update):
        '''Recebe o id, o nome do atributo e o atributo update e atualiza o atributo com o  valor do update.'''
        Aluguel.tabela_aluguel()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute(f'''UPDATE aluguel
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id))
        
        conexao.commit()
        cursor.close()
        conexao.close() 

    def delete():
        print("\nFunção em desenvolcimento\n")

    def calcular_multa(self, dias):
        '''Recebe o valor da multa por atraso diária, os dias de atraso e calcula o valor da multa.'''
        multa = dias * self.multa_diaria
        return multa
    
    def calculo_aluguel_externo(self, dias):
        '''Recebe o ID do jogo alugado externamente e os dias pelos quais ele vai ser alugado e retorna o valor do aluguel'''
        diaria = Jogo_aluguel(self.id_jogo_aluguel)[10]
        aluguel_externo = diaria * dias
        return aluguel_externo
    
    def calculo_aluguel_interno(self, quantidade_sessoes):
        '''Recebe o ID do jogo alugado internamente e a quantidade de sessões pelas quais ele vai ser alugado e retorna o valor do aluguel'''
        valor_sessao = Jogo_aluguel(self.id_jogo_aluguel)[9]
        aluguel_interno = valor_sessao * quantidade_sessoes
        return aluguel_interno
