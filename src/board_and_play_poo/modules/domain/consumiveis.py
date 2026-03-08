from .produtos import Produto

class Consumivel(Produto):
    '''Classe que cuida dos consumíveis (alimentos prontos, bebidas)'''
    def __init__(self, nome, codigo_barras, categoria, data_validade, lote, restricoes, quantidade, produto_id = None, consumivel_id = None):
        super().__init__(nome, codigo_barras, categoria, produto_id)
        self.data_validade = data_validade
        self.lote = lote
        self.restricoes = restricoes
        self.quantidade = quantidade
        self.consumivel_id = consumivel_id

    def __str__(self):
        return f"ID do consumivel: {self.consumivel_id}\nID de produto desse consumivel: {self.produto_id}\nData de validade: {self.data_validade}\nLote a que pertence: {self.lote}\nRestrições: {self.restricoes}\n Quantidade disponível: {self.quantidade}"