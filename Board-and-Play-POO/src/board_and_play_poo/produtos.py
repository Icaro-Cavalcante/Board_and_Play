class Produto:
    '''Descreve um produto'''

    def __init__(self, id, nome, preco):
        self.__nome = nome
        self.__id = id
        self.preco = preco