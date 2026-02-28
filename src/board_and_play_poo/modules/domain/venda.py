from pathlib import Path
from .transacoes import Transacao
#from .compraveis import Jogo_venda
  

class Venda(Transacao):
    def __init__(self, id_transacao, id_cliente, id_colaborador, nota_fiscal, id_venda = None):
        self.id_transacao = id_transacao
        self.id_venda = id_venda
        self.id_cliente = id_cliente
        self.id_colaborador = id_colaborador
        self.nota_fiscal = nota_fiscal
    """
    @property
    def id_venda(self) -> int:
        '''getter para importar o __id_venda encapsulado em outras classes'''
        return self.__id_venda"""

    def __str__(self):
        return f"ID da Venda: {self.id_venda} | ID da transação: {self.id_transacao} | ID do Cliente: {self.id_cliente}\nQID do Colaborador: {self.id_colaborador} | Nota Fiscla: {self.nota_fiscal}"
    
    def __eq__(self, outro):
        return self.id_venda == outro.id_venda
    
    """def calcular_venda(self, quantidade):
        '''Recebe o ID do produto a ser comprado e a quantidade e retorna o valor da venda'''
        tupla = Jogo_venda.read(self.id_produto)
        objeto = Jogo_venda.tupla_objeto(tupla)
        valor_compra = objeto._valor_compra
        venda = valor_compra * quantidade
        return venda"""
