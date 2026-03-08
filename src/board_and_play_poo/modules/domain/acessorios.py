from .produtos import Produto

class Acessorio(Produto):
    '''Classe que cuida de todos os produtos do tipo acessorio.'''
    def __init__(self, nome, codigo_barras, categoria, tipo_acessorio, quantidade, produto_id = None, acessorio_id = None):
        super().__init__(nome, codigo_barras, categoria, produto_id)
        self.__tipo_acessorio = tipo_acessorio
        self.__quantidade = quantidade
        self.__acessorio_id = acessorio_id

    @property
    def acessorio_id(self):
        return self.__acessorio_id
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def tipo_acessorio(self):
        return self.__tipo_acessorio

    def __str__(self):
        return f"ID do acessorio: {self.__id}\nID de produto desse acessorio: {self.__produto_id}\nTipo do acessorio: {self.__tipo_acessorio}\nQuantidade em estoque: {self.__quantidade}"