from .produtos import Produto

class Consumivel(Produto):
    '''Classe que cuida dos consumíveis (alimentos prontos, bebidas)'''
    def __init__(self, nome, codigo_barras, categoria, data_validade, lote, restricoes, quantidade, produto_id = None, consumivel_id = None):
        super().__init__(nome, codigo_barras, categoria, produto_id)
        self.__data_validade = data_validade
        self.__lote = lote
        self.__restricoes = restricoes
        self.__quantidade = quantidade
        self.__consumivel_id = consumivel_id
    
    @property
    def data_validade(self):
        return self.__data_validade
    
    @property
    def lote(self):
        return self.__lote

    @property
    def restricoes(self):
        return self.__restricoes

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def consumivel_id(self):
        return self.__consumivel_id

    def __str__(self):
        return f"ID do consumivel: {self.__consumivel_id}\nID de produto desse consumivel: {self.__produto_id}\nData de validade: {self.__data_validade}\nLote a que pertence: {self.__lote}\nRestrições: {self.__restricoes}\n Quantidade disponível: {self.__quantidade}"