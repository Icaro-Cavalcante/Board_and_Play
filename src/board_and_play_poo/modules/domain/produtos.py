from abc import ABC

class Produto(ABC):
    '''
    Integra atributos em comum de suas subclasses, servindo como generalização
    '''

    def __init__(self, nome, codigo_barras, categoria, produto_id=None): # O ID não deve ser passado como parâmetro
        self._nome = nome
        self._codigo_barras = codigo_barras
        self._categoria = categoria
        self._produto_id = produto_id

    @property
    def nome(self):
        return self._nome
    
    @property
    def codigo_barras(self):
        return self._codigo_barras

    @property
    def categoria(self):
        return self._categoria

    @property
    def produto_id(self):
        return self._produto_id

    @nome.setter
    def nome(self, novo_valor):
        self._nome = novo_valor

    @codigo_barras.setter
    def codigo_barras(self, novo_valor):
        self._codigo_barras = novo_valor

    @categoria.setter
    def categoria(self, novo_valor):
        self._categoria = novo_valor

    @produto_id.setter
    def produto_id(self, novo_valor):
        self._produto_id = novo_valor
