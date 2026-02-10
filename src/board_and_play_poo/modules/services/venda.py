from pathlib import Path
from ..domain.produtos import Produto
import sqlite3
caminho_data = "src/board_and_play_poo/data/dados.db"

class Venda():
    def __init__(self, id_venda, id_produto, tipo_produto):
        self.__id_venda = id_venda
        self.id_produto = id_produto
        self.tipo_produto = tipo_produto

    @property
    def id_venda(self) -> int:
        '''getter para importar o __id_venda encapsulado em outras classes'''
        return self.__id_venda

    def __str__(self):
        return f"ID da Venda: {self.id_venda}\nID do produto comprado: {self.id_produto}\nTipo do produto comprado: {self.tipo_produto}"
    
    def __eq__(self, outro):
        return self.id_venda == outro.id_venda
    
    def pasta_database():
        '''Método que cria a pasta (data) de dados, caso ela não exista'''
        caminho_diretorio = r"src/board_and_play_poo/data"
        caminho_diretorio = Path(caminho_diretorio)
        caminho_diretorio.mkdir(exist_ok=True)

    def tabela_venda():
        '''Cria a tabela de itens vendidos no banco de dados'''
        Venda.pasta_database()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS venda 
                       (id_venda INTEGER UNIQUE, id_produto INTEGER, tipo TEXT)''')

        cursor.close()
        conexao.close()

    def create():
        '''Recebe os atributos de venda e os registra no banco de dados'''
        novo_id_venda = int(input("Informe o ID da venda: "))
        novo_id_produto = int(input("Informe o ID do produto comprado: "))
        novo_tipo_produto = str(input("Informe o tipo do produto: "))

        nova_venda = Venda(novo_id_venda, novo_id_produto, novo_tipo_produto)

        Venda.tabela_venda()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''INSERT OR IGNORE INTO venda 
                       (id_venda, id_produto, tipo_produto)
                       VALUES (?, ?, ?)''', (nova_venda.id_venda, nova_venda.id_produto, nova_venda.tipo_produto))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("\nVenda criada.\n")

    def read(id):
        '''Recebe o id de venda e retorna uma tupla com os dados dela.'''
        Venda.tabela_venda()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM venda WHERE id_venda = ?''', (id, ))
        venda = cursor.fetchone()

        cursor.close()
        conexao.close()
        return venda

    def update(id, nome_atributo, atributo_update):
        '''Recebe o id, o nome do atributo e o atributo update e atualiza o atributo com o  valor do update.'''
        Venda.tabela_venda()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute(f'''UPDATE venda
                    SET {nome_atributo} = ?
                    WHERE id = ?''', (atributo_update, id))
        
        conexao.commit()
        cursor.close()
        conexao.close() 

# Não sei dizer onde exatamente seria utilizado um Delete uma vez que, por RN, precisamos manter todos esses dados no banco
# Talvez o CRUD seja apenas um CRU

    def delete():
        print("\nFunção em desenvolvimento\n")

    def calcular_venda(self, quantidade):
        '''Recebe o ID do produto a ser comprado e a quantidade e retorna o valor da venda'''
        valor_compra = Produto(self.id_produtoa)[8]
        venda = valor_compra * quantidade
        return  venda