from .jogos import Jogo
import sqlite3
caminho_data = r"src/board_and_play_poo/data/dados.db"

class Jogo_aluguel(Jogo):
    '''
    A classe dos jogos alugáveis. Ela cuida do CRUD 
    '''
    def __init__(self, id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_sessao, valor_diaria):
        super().__init__(id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status)
        self.__valor_sessao = valor_sessao
        self.__valor_diaria = valor_diaria

    def __str__(self):
         return f"ID: {self.id}\nNome: {self.nome}\nCusto de aquisição: {self._custo_aquisicao}\nDescrição: {self._descricao}\nIdade mínima: {self._idade_min}\nNúmero de jogadores: {self._num_jogadores}\nTipo: {self.tipo}\nStatus: {self._status}"

    def __eq__(self, outro):
         return self.id == outro.id
    
    def tabela_jogo_aluguel():
      '''Cria a tabela de jogos alugáveis no banco de dados'''
      Jogo_aluguel.pasta_database()
      conexao = sqlite3.connect(caminho_data)
      cursor = conexao.cursor()
      cursor.execute('''CREATE TABLE jogo_aluguel IF NOT EXISTS(id INTEGER UNIQUE, nome TEXT, custo_aquisicao REAL, descricao TEXT, idade_min INTEGER, num_jogadores INTEGER, tipo TEXT, status TEXT, valor_sessao REAL, valor_diaria REAL)''')
      
      cursor.close()
      conexao.close()
    
    def create():
         '''Recebe os atributos do jogo alugável e registra ele no banco de dados'''
         novo_id = int(input("Informe o id do jogo alugável: "))
         novo_nome = str(input("Informe o nome do jogo alugável: "))
         novo_custo = float(input("Informe o id do jogo alugável: "))
         nova_data = str(input("Informe a data de aquisição do jogo alugável: "))
         nova_descricao = int(input("Informe a descrição do jogo alugável: "))
         nova_idade = int(input("Informe a idade mínima do jogo alugável: "))
         novo_num = int("Informe o número de jogadores do jogo alugável: ")
         novo_tipo= int("Informe o tipo do jogo alugável: ")
         novo_status = int("Informe o status do jogo alugável: ")
         novo_sessao = int("Informe o valor da sessão do jogo alugável: ")
         novo_diaria = int("Informe o valor da diária do jogo alugável: ")

         novo_jogo = Jogo(novo_id, novo_nome, novo_custo, nova_data, nova_descricao, nova_idade, novo_num, novo_tipo, novo_status, novo_sessao, novo_diaria)

         Jogo_aluguel.tabela_jogo_aluguel()
         conexao = sqlite3.connect(caminho_data)
         cursor = conexao.cursor()
         cursor.execute('''INSERT OR IGNORE INTO jogo_aluguel
                       (id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_sessao, valor_diaria)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (novo_jogo.novo_id, novo_jogo.novo_nome, novo_jogo.novo_custo, novo_jogo.nova_data, novo_jogo.nova_descricao, novo_jogo.nova_idade, novo_jogo.novo_num, novo_jogo.novo_tipo, novo_jogo.novo_status, novo_jogo.novo_sessao, novo_jogo.novo_diaria))
         conexao.commit()
         cursor.close()
         conexao.close()

         print("\n Jogo criado\n")

    def read(id):
          '''Recebe o id do jogo alugável e retorna uma tupla com os dados dele.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''SELECT * FROM jogo_aluguel WHERE id = ?''', (id))
          jogo_alugavel = cursor.fetchone()

          cursor.close()
          conexao.close()
          return jogo_alugavel
    
    def update(id, nome_atributo, atributo_update):
          '''Recebe o id, o nome do atributo e o atributo update e atualiza o atributo com o  valor do update.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute(f'''UPDATE jogo_aluguel
                        SET {nome_atributo} = ?
                        WHERE id = ?''', (atributo_update, id))
          
          conexao.commit()
          cursor.close()
          conexao.close() 
    
    def delete(id):
          '''Recebe o id do jogo alugável e atualiza seu status para inativo.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''UPDATE jogo_aluguel
                        SET status = ?
                        WHERE id = ?''', ("inativo", id))
          
          conexao.commit()
          cursor.close()
          conexao.close()