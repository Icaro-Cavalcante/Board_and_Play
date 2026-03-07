import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime
""" from aluguel import Aluguel
from venda import Venda """
from pathlib import Path
caminho_data = "src/board_and_play_poo/data/dados.db"

class Transacao(ABC):
    def __init__(self, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao , transacao_id = None):
        self.transacao_id = transacao_id
        self.comprovante = comprovante
        self.data_hora = data_hora
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.tipo_transacao = tipo_transacao

    def __str__(self):
        return f"ID da transação: {self.id} | ID do cliente: {self.id_cliente} | ID do colaborador: {self.id_colaborador}\n"

    @abstractmethod
    def calcular_valor(self, obj_negocio):
        pass

    @abstractmethod
    def gerar_comprovante(self, obj_negocio): #????????????
        pass

    @abstractmethod
    def tempo_atual(self, obj_negocio):
        pass

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

