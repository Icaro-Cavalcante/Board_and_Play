from abc import ABC

class Produto(ABC):
    '''
    Integra atributos em comum de suas subclasses, servindo como generalização
    '''

    def __init__(self, nome, codigo_barras, categoria, quantidade, id=None): # O ID não deve ser passado como parâmetro
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.quantidade = quantidade
        self.id = id