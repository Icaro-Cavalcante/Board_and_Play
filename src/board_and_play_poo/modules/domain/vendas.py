import random
from .transacoes import Transacao
from src.board_and_play_poo.modules.infrastructure.descontos import DescontoPorcent, DescontoValorFixo

class Venda(Transacao):
    """Classe responsável pelas transações de venda"""
    def __init__(self, cliente_id, colaborador_id, nota_fiscal, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, transacao_id, venda_id = None):
        super().__init__(comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao , transacao_id)
        self.__venda_id = venda_id
        self.__cliente_id = cliente_id
        self.__colaborador_id = colaborador_id
        self.__nota_fiscal = nota_fiscal

    @property
    def id_transacao(self): 
        return self._transacao_id

    @property
    def id_cliente(self): 
        return self.__cliente_id

    @property
    def id_colaborador(self): 
        return self.__colaborador_id

    @property
    def nota_fiscal(self):
        return self.__nota_fiscal

    def __str__(self):
        return f"ID da Venda: {self.__venda_id} | ID da transação: {self._transacao_id} | ID do Cliente: {self.__cliente_id}\nQID do Colaborador: {self.__colaborador_id} | Nota Fiscla: {self.__nota_fiscal}"
    
    def calcular_valor(preco, unidades):
        return preco * unidades
    
    def gerar_comprovante():
        return f"Venda:{random.randint(1, 99999999999999)}"
    
    def AplicarDesconto(valor: float, tipo: str):
        """Aplica desconto ao valor passado baseado no tipo, tipo deve ser ou 'porcentagem' ou 'valorfixo', não case sensitive"""
        if tipo.lower() == "porcentagem":
            while True:
                try:
                    porcent = int(input("Digite a porcentagem do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoPorcent(porcent)
            valor = descont.AplicarDesconto(valor)
            return valor
        if tipo.lower() == "valorfixo":
            while True:
                try:
                    vfixo = float(input("Digite o valor do desconto do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoValorFixo(vfixo)
            valor = descont.AplicarDesconto(valor)
            return valor
