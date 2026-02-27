from pathlib import Path
from .transacoes import Transacao
#from .compraveis import Jogo_venda

class Venda(Transacao):
    def __init__(self, id_venda, id_produto, tipo_produto, id_transacao, id_cliente, id_colaborador, nota_fiscal):
        super(self.__init__(id_transacao, id_cliente, id_colaborador, nota_fiscal))
        self.__id_venda = id_venda
        self.id_produto = id_produto
        self.tipo_produto = tipo_produto

    @property
    def id_venda(self) -> int:
        '''getter para importar o __id_venda encapsulado em outras classes'''
        return self.__id_venda

    def __str__(self):
        return f"ID da Venda: {self.id_venda}\nID do produto comprado: {self.id_produto}\nTipo do produto comprado: {self.tipo_produto}"
    
    def __eq__(self, outro):
        return self.id_venda == outro.id_venda
    
    """def calcular_venda(self, quantidade):
        '''Recebe o ID do produto a ser comprado e a quantidade e retorna o valor da venda'''
        tupla = Jogo_venda.read(self.id_produto)
        objeto = Jogo_venda.tupla_objeto(tupla)
        valor_compra = objeto._valor_compra
        venda = valor_compra * quantidade
        return venda"""
