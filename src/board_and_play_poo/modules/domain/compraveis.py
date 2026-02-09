from .jogos import Jogo
import sqlite3
caminho_data = r"src/board_and_play_poo/data/dados.db"

class Jogo_venda(Jogo):
    '''
    A classe dos jogos compráveis. Ela cuida do CRUD 
    '''
    def __init__(self, id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_compra):
          super().__init__(id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status)
          self.__valor_compra = valor_compra

    def __str__(self):
         return f"ID: {self.id}\nNome: {self.nome}\nCusto de aquisição: {self._custo_aquisicao}\nDescrição: {self._descricao}\nIdade mínima: {self._idade_min}\nNúmero de jogadores: {self._num_jogadores}\nTipo: {self.tipo}\nStatus: {self._status}"

    def __eq__(self, outro):
         return self.id == outro.id
    
    def tabela_jogo_venda():
      '''Cria a tabela de jogos alugáveis no banco de dados'''
      Jogo_venda.pasta_database()
      conexao = sqlite3.connect(caminho_data)
      cursor = conexao.cursor()
      cursor.execute('''CREATE TABLE jogo_compra IF NOT EXISTS(id INTEGER UNIQUE, nome TEXT, custo_aquisicao REAL, descricao TEXT, idade_min INTEGER, num_jogadores INTEGER, tipo TEXT, status TEXT, valor_compra REAL)''')
      
      cursor.close()
      conexao.close()
    
    def create():
         '''Recebe os atributos do jogo alugável e registra ele no banco de dados'''
         novo_id = int(input("Informe o id do jogo comprável: "))
         novo_nome = str(input("Informe o nome do jogo comprável: "))
         novo_custo = float(input("Informe o custo de aquisição do jogo comprável: "))
         nova_data = str(input("Informe a data de aquisição do jogo comprável: "))
         nova_descricao = str(input("Informe a descrição do jogo comprável: "))
         nova_idade = int(input("Informe a idade mínima do jogo comprável: "))
         novo_num = int(input("Informe o número de jogadores do jogo comprável: "))
         novo_tipo= str(input("Informe o tipo do jogo comprável: "))
         novo_status = str(input("Informe o status do jogo comprável: "))
         novo_preco = float(input("Informe o valor do jogo comprável: "))

         novo_jogo = Jogo(novo_id, novo_nome, novo_custo, nova_data, nova_descricao, nova_idade, novo_num, novo_tipo, novo_status, novo_preco)

         Jogo_venda.tabela_jogo_venda()
         conexao = sqlite3.connect(caminho_data)
         cursor = conexao.cursor()
         cursor.execute('''INSERT OR IGNORE INTO jogo_aluguel
                       (id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_compra)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (novo_jogo.novo_id, novo_jogo.novo_nome, novo_jogo.novo_custo, novo_jogo.nova_data, novo_jogo.nova_descricao, novo_jogo.nova_idade, novo_jogo.novo_num, novo_jogo.novo_tipo, novo_jogo.novo_status, novo_jogo.novo_preco))
         conexao.commit()
         cursor.close()
         conexao.close()

         print("\n Jogo criado\n")

    def read(id):
          '''Recebe o id do jogo alugável e retorna uma tupla com os dados dele.'''
          Jogo_venda.tabela_jogo_venda()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''SELECT * FROM jogo_venda WHERE id = ?''', (id))
          jogo_compravel = cursor.fetchone()

          cursor.close()
          conexao.close()
          return jogo_compravel
    
    def update(id, nome_atributo, atributo_update):
          '''Recebe o id, o nome do atributo e o atributo update e atualiza o atributo com o  valor do update.'''
          Jogo_venda.tabela_jogo_venda()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute(f'''UPDATE jogo_venda
                        SET {nome_atributo} = ?
                        WHERE id = ?''', (atributo_update, id))
          
          conexao.commit()
          cursor.close()
          conexao.close() 
    
    def delete(id):
          '''Recebe o id do jogo alugável e atualiza seu status para inativo.'''
          Jogo_venda.tabela_jogo_venda()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''UPDATE jogo_venda
                        SET status = ?
                        WHERE id = ?''', ("inativo", id))
          
          conexao.commit()
          cursor.close()
          conexao.close()