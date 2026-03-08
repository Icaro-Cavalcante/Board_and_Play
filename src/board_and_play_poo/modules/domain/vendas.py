from pathlib import Path
from .transacoes import Transacao
from board_and_play_poo.modules.infrastructure.descontos import DescontoPorcent, DescontoValorFixo

class Venda(Transacao):
    def __init__(self, cliente_id, colaborador_id, nota_fiscal, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, venda_id = None, transacao_id = None):
        super().__init__(self, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, transacao_id)
        self.__venda_id = venda_id
        self.__cliente_id = cliente_id
        self.__colaborador_id = colaborador_id
        self.__nota_fiscal = nota_fiscal

    @property
    def venda_id(self):
        return self.__venda_id

    @property
    def cliente_id(self):
        return self.__cliente_id

    @property
    def colaborador_id(self):
        return self.__colaborador_id

    @property
    def nota_fiscal(self):
        return self.__nota_fiscal

    def __str__(self):
        return f"ID da Venda: {self.__id_venda} | ID da transação: {self.__id_transacao} | ID do Cliente: {self.__id_cliente}\nQID do Colaborador: {self.__id_colaborador} | Nota Fiscla: {self.__nota_fiscal}"
    
    def calcular_valor(self, preco, unidades):
        """Calcula valor final para u, jogo que está sendo vendido"""
        return preco * unidades
    
    def AplicarDesconto(self, valor: float, tipo: str):
        """Aplica desconto ao valor passado baseado no tipo, tipo deve ser ou 'porcentagem' ou 'valorfixo', não case sensitive"""
        if tipo.lower == "porcentagem":
            while True:
                try:
                    porcent = int(input("Digite a porcentagem do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoPorcent(porcent)
            valor = descont.AplicarDesconto(valor)
            return valor
        if tipo.lower == "valorfixo":
            while True:
                try:
                    vfixo = int(input("Digite o valor do desconto do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoValorFixo(vfixo)
            valor = descont.AplicarDesconto(valor)
            return valor
