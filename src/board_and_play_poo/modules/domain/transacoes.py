import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime
""" from aluguel import Aluguel
from venda import Venda """
from pathlib import Path
caminho_data = "src/board_and_play_poo/data/dados.db"

class Transacao(ABC):
    def __init__(self, data_hora, valor_total, forma_pagamento, status_pagamento, tipo_transacao , id = None):
        self.id = id
        self.data_hora = data_hora
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.status_pagamento = status_pagamento
        self.tipo_transacao = tipo_transacao

    def __str__(self):
        return f"ID da transação: {self.id} | ID do cliente: {self.id_cliente} | ID do colaborador: {self.id_colaborador}\n"
'''
    @abstractmethod
    def calcular_valor(self, obj_negocio):
        pass
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
        return valor'''
'''
    @abstractmethod
    def calcular_multa(self, obj_negocio):
        pass
        try:
            if obj_negocio.id_venda:
                return 0
            elif obj_negocio.id_aluguel:
                valor = Aluguel.calcular_multa(int(input("Digite a quantia de dias além do prazo estipulado(0 se nenhum): ")))
        except AttributeError:
            return print("Tentativa de cálculo de multa falhou, tente repassar um aluguel existente e ativo.")
        return valor'''

