import sqlite3
from abc import ABC, abstractmethod

class Transacao(ABC):
    """Classe abstrata que entrega atributos e métodos para Venda e Aluguel"""
    def __init__(self, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao , transacao_id = None):
        self._transacao_id = transacao_id
        self._comprovante = comprovante
        self._data_hora = data_hora
        self._valor_total = valor_total
        self._forma_pagamento = forma_pagamento
        self._tipo_transacao = tipo_transacao

    @property
    def transacao_id(self):
        return self._transacao_id
    
    @property
    def comprovante(self):
        return self._comprovante
    
    @property
    def data_hora(self):
        return self._data_hora
    
    @property
    def valor_total(self):
        return self._valor_total
    
    @property
    def forma_pagamento(self):
        return self._forma_pagamento
    
    @property
    def tipo_transacao(self):
        return self._tipo_transacao
    
    def __str__(self):
        return f"ID da transação: {self._id} | ID do cliente: {self._id_cliente} | ID do colaborador: {self._id_colaborador}\n"

    @abstractmethod
    def calcular_valor(self, preco):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass