import sqlite3
from aluguel import Aluguel
from venda import Venda
from pathlib import Path
caminho_data = "src/board_and_play_poo/data/dados.db"

class Transacao:
    def __init__(self, id_transacao, id_negocio, valor_final, metodo, multa_avaria):
        self.__id_transacao = id_transacao
        self.__id_negocio = id_negocio
        self.__valor_final = valor_final
        self.__metodo = metodo
        self.__multa_avaria = multa_avaria

    def __str__(self):
        return f"ID da transação: {self.id_transacao}\nID de aluguel/venda: {self.id_negocio}\nValor da transação: {self.valor_final}\nMétodo de pagamento: {self.metodo}\nMulta de avaria: {self.multa_avaria}"
    
    def pasta_database():
        '''Método que cria a pasta (data) de dados, caso ela não exista'''
        caminho_diretorio = r"src/board_and_play_poo/data"
        caminho_diretorio = Path(caminho_diretorio)
        caminho_diretorio.mkdir(exist_ok=True)

    def tabela_transacao():
        '''Cria a tabela de transações no banco de dados'''
        Transacao.pasta_database()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS transacao 
                       (id_transacao INTEGER UNIQUE, id_negocio INTEGER, valor_final REAL, metodo TEXT, multa_avaria REAL)''')
        cursor.close()
        conexao.close()

    def create(self, obj_negocio):
        '''Recebe os atributos da transação e registra ela no banco de dados'''
        novo_id_transacao = int(input("Informe o ID da transação: "))
        novo_id_negocio = int(input("Informe o ID do negócio para comprovante: "))
        novo_valor_final = self.calcular_valor(obj_negocio)
        novo_metodo = str(input("Informe a forma de pagamento: "))
        nova_multa_avaria = self.calcular_multa(obj_negocio)

        nova_transacao = Transacao(novo_id_transacao, novo_id_negocio, novo_valor_final, novo_metodo, nova_multa_avaria)

        Transacao.tabela_transacao()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''INSERT OR IGNORE INTO transacao
                       (id_transacao, id_negocio, valor_final, metodo, multa_avaria)
                       VALUES (?, ?, ?, ?, ?)''', (nova_transacao.id_transacao, nova_transacao.id_negocio, nova_transacao.valor_final, nova_transacao.metodo, nova_transacao.multa_avaria))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("\nComprovante criado.\n")
        
    def read(id):
        '''Recebe o id da transação e retorna uma tupla com os dados dela.'''
        Transacao.tabela_transacao()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM transacao WHERE id_transacao = ?''', (id, ))
        transacao = cursor.fetchone()
        cursor.close()
        conexao.close()
        return transacao

    def calcular_valor(self, obj_negocio):
        try:
            if obj_negocio.id_aluguel:
                escolha = int(input("\n1 - Aluguel interno\n2 - Aluguel externo"))
                match escolha:
                    case 1:
                        valor = Aluguel.calculo_aluguel_interno(int(input("\nDigite quantas sessões serão ofertadas: ")))
                    case 2:
                        valor = Aluguel.calculo_aluguel_externo(int(input("\nDigite a quantia de dias para locação: ")))
                    case _:
                        print("Escolha inválida, saindo de menu de cálculo.\n")
            elif obj_negocio.id_venda:
                valor = Venda.calcular_venda(int(input("Digite a quantia deste produto a ser comprado: ")))
        except AttributeError:
            return print("Tentativa de cálculo de valor falhou, tente repassar um aluguel/venda existente e ativo.")
        return valor
    
    def calcular_multa(self, obj_negocio):
        try:
            if obj_negocio.id_venda:
                return 0
            elif obj_negocio.id_aluguel:
                valor = Aluguel.calcular_multa(int(input("Digite a quantia de dias além do prazo estipulado(0 se nenhum): ")))
        except AttributeError:
            return print("Tentativa de cálculo de multa falhou, tente repassar um aluguel existente e ativo.")
        return valor

