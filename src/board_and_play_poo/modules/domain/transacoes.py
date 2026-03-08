import sqlite3
from abc import ABC, abstractmethod

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
    def calcular_valor(self, preco):
        pass

    @abstractmethod
    def gerar_comprovante(self): #????????????
        pass