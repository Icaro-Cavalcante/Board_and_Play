from .jogos import Jogo
import sqlite3
caminho_data = r"src/board_and_play_poo/data/dados.db"

class Jogo_aluguel(Jogo):
    '''
    A classe dos jogos alugáveis. Ela cuida do CRUD 
    '''
    def __init__(self, id_produto, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_sessao, valor_diaria):
        super().__init__(id_produto, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status)
        self._valor_sessao = valor_sessao
        self._valor_diaria = valor_diaria

    def __str__(self):
         return f"ID: {self.id_produto}\nNome: {self.nome}\nCusto de aquisição: {self._custo_aquisicao}\nDescrição: {self._descricao}\nIdade mínima: {self._idade_min}\nNúmero de jogadores: {self._num_jogadores}\nTipo: {self.tipo}\nStatus: {self._status}"

    def __eq__(self, outro):
         return self.id_produto == outro.id_produto
    
    def tabela_jogo_aluguel():
      '''Cria a tabela de jogos alugáveis no banco de dados'''
      Jogo_aluguel.pasta_database()
      conexao = sqlite3.connect(caminho_data)
      cursor = conexao.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS jogo_aluguel (id_produto INTEGER UNIQUE, nome TEXT, custo_aquisicao REAL, data_aquisicao TEXT, descricao TEXT, idade_min INTEGER, num_jogadores INTEGER, tipo TEXT, status TEXT, valor_sessao REAL, valor_diaria REAL)''')

      cursor.close()
      conexao.close()
    
    def create():
         '''Recebe os atributos do jogo alugável e registra ele no banco de dados'''
         novo_id = int(input("Informe o id do jogo alugável: "))
         novo_nome = str(input("Informe o nome do jogo alugável: "))
         novo_custo = float(input("Informe o custo do jogo alugável: "))
         nova_data = str(input("Informe a data de aquisição do jogo alugável: "))
         nova_descricao = str(input("Informe a descrição do jogo alugável: "))
         nova_idade = int(input("Informe a idade mínima do jogo alugável: "))
         novo_num = int(input("Informe o número de jogadores do jogo alugável: "))
         novo_tipo= str(input("Informe o tipo do jogo alugável: "))
         novo_status = str(input("Informe o status do jogo alugável: "))
         novo_sessao = float(input("Informe o valor da sessão do jogo alugável: "))
         novo_diaria = float(input("Informe o valor da diária do jogo alugável: "))

         novo_jogo = Jogo_aluguel(novo_id, novo_nome, novo_custo, nova_data, nova_descricao, nova_idade, novo_num, novo_tipo, novo_status, novo_sessao, novo_diaria)

         Jogo_aluguel.tabela_jogo_aluguel()
         conexao = sqlite3.connect(caminho_data)
         cursor = conexao.cursor()
         cursor.execute('''INSERT OR IGNORE INTO jogo_aluguel
                       (id_produto, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status, valor_sessao, valor_diaria)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (novo_jogo._id_produto, novo_jogo._nome, novo_jogo._custo_aquisicao, novo_jogo._data_aquisicao, novo_jogo._descricao, novo_jogo._idade_min, novo_jogo._num_jogadores, novo_jogo._tipo, novo_jogo._status, novo_jogo._valor_sessao, novo_jogo._valor_diaria))
         conexao.commit()
         cursor.close()
         conexao.close()

         print("\n Jogo criado\n")
         return "Sucesso! Jogo criado."

    def read(id_produto):
          '''Recebe o id do jogo alugável e retorna uma tupla com os dados dele.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''SELECT * FROM jogo_aluguel WHERE id_produto = ?''', (id_produto, ))
          jogo_alugavel = cursor.fetchone()

          cursor.close()
          conexao.close()
          return jogo_alugavel
    
    def update(id_produto, nome_atributo, atributo_update):
          '''Recebe o id, o nome do atributo e o atributo update e atualiza o atributo com o  valor do update.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute(f'''UPDATE jogo_aluguel
                        SET {nome_atributo} = ?
                        WHERE id_produto = ?''', (atributo_update, id_produto))
          
          conexao.commit()
          cursor.close()
          conexao.close() 
    
    def delete(id_produto):
          '''Recebe o id do jogo alugável e atualiza seu status para inativo.'''
          Jogo_aluguel.tabela_jogo_aluguel()
          conexao = sqlite3.connect(caminho_data)
          cursor = conexao.cursor()
          cursor.execute('''UPDATE jogo_aluguel
                        SET status = ?
                        WHERE id_produto = ?''', ("inativo", id_produto))
          
          conexao.commit()
          cursor.close()
          conexao.close()