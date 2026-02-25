import sqlite3
from .aluguel import Aluguel
from .venda import Venda
from pathlib import Path
caminho_data = "src/board_and_play_poo/data/dados.db"

class Transacao:
    def __init__(self, id_transacao, id_negocio, valor_final, metodo, multa_avaria):
        self.__id_transacao = id_transacao
        self.__id_negocio = id_negocio
        self.__valor_final = valor_final
        self.metodo = metodo
        self.__multa_avaria = multa_avaria

    def __str__(self):
        return f"ID da transação: {self.__id_transacao}\nID de aluguel/venda: {self.__id_negocio}\nValor da transação: {self.__valor_final}\nMétodo de pagamento: {self.metodo}\nMulta de avaria: {self.__multa_avaria}"
    
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

    def create(obj_negocio):
        '''Recebe os atributos da transação e registra ela no banco de dados'''
        novo_id_transacao = int(input("Informe o ID da transação: "))
        novo_id_negocio = int(input("Informe o ID do negócio para comprovante: "))
        while True:
            try:
                if obj_negocio.id_aluguel:
                    escolha = int(input("\n1 - Aluguel interno\n2 - Aluguel externo\n"))
                    break
            except AttributeError:
                if obj_negocio.id_venda:
                    escolha = 3
                    break
                print("\nInput inválido, digite novamente.\n")
        novo_valor_final = Transacao.calcular_valor(obj_negocio, escolha)
        novo_metodo = str(input("Informe a forma de pagamento: "))
        nova_multa_avaria = Transacao.calcular_multa(obj_negocio)

        nova_transacao = Transacao(novo_id_transacao, novo_id_negocio, novo_valor_final, novo_metodo, nova_multa_avaria)

        Transacao.tabela_transacao()
        conexao = sqlite3.connect(caminho_data)
        cursor = conexao.cursor()
        cursor.execute('''INSERT OR IGNORE INTO transacao
                       (id_transacao, id_negocio, valor_final, metodo, multa_avaria)
                       VALUES (?, ?, ?, ?, ?)''', (nova_transacao.__id_transacao, nova_transacao.__id_negocio, nova_transacao.__valor_final, nova_transacao.metodo, nova_transacao.__multa_avaria))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Comprovante criado.")
        return "\nComprovante criado.\n"
        
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
    
    def tupla_objeto(tupla):
         '''Transforma a tupla retornada no método read em um objeto'''
         transacao = Transacao(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
         return transacao

    def calcular_valor(obj_negocio, escolha):
        match escolha:
            case 1:
                valor = obj_negocio.calculo_aluguel_interno(int(input("\nDigite quantas sessões serão ofertadas: ")))
            case 2:
                valor = obj_negocio.calculo_aluguel_externo(int(input("\nDigite a quantia de dias para locação: ")))
            case 3:
                valor = obj_negocio.calcular_venda(int(input("\nDigite a quantia deste produto a ser comprado: ")))
        return valor
    
    def calcular_multa_dias(obj_negocio):
        valor = 0
        while True:
            try:
                if obj_negocio.id_aluguel:
                    valor = obj_negocio.calcular_multa(int(input("Digite a quantia de dias além do prazo estipulado(0 se nenhum)\n")))
                    break
            except AttributeError:
                if not obj_negocio.id_venda:
                    print("\nTentativa de cálculo de multa falhou, digite novamente.\n")
                else: break
        return valor
    
    def calcular_multa_avaria(obj_negocio):
        valor = 0
        while True:
            try:
                if obj_negocio.id_aluguel:
                    escolha = int(input("Houve danos ao produto durante a locação?\n1 - Sim\n2 - Não\n"))
                    break
            except AttributeError: 
                if not obj_negocio.id_venda:
                    print("\nInput inválido, digite novamente.\n")
                else: break
            if escolha == 1: valor = obj_negocio.multa_avaria
        return valor

    def calcular_multa(obj_negocio):
        avaria = Transacao.calcular_multa_avaria(obj_negocio)
        dias = Transacao.calcular_multa_dias(obj_negocio)
        multa = dias + avaria
        return multa
