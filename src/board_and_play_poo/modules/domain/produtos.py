from abc import ABC

class Produto(ABC):
    '''
    Integra atributos em comum de suas subclasses, servindo como generalização
    '''

    def __init__(self, nome, codigo_barras, categoria, produto_id=None): # O ID não deve ser passado como parâmetro
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.produto_id = produto_id