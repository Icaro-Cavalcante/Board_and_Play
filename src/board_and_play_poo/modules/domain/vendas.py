from pathlib import Path
from .transacoes import Transacao
from src.board_and_play_poo.modules.infrastructure.desconto import DescontoPorcent, DescontoValorFixo

class Venda(Transacao):
    def __init__(self, id_cliente, id_colaborador, nota_fiscal, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, venda_id = None, transacao_id = None):
        super().__init__(self, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, transacao_id)
        self.transacao_id = transacao_id
        self.venda_id = venda_id
        self.id_cliente = id_cliente
        self.id_colaborador = id_colaborador
        self.nota_fiscal = nota_fiscal
        self.comprovante = comprovante
        self.data_hora = data_hora
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.tipo_transacao = tipo_transacao

    def __str__(self):
        return f"ID da Venda: {self.id_venda} | ID da transação: {self.id_transacao} | ID do Cliente: {self.id_cliente}\nQID do Colaborador: {self.id_colaborador} | Nota Fiscla: {self.nota_fiscal}"
    
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
