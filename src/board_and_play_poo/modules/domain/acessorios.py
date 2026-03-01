from .produtos import Produto

class Acessorio(Produto):
    '''Classe que cuida de todos os produtos do tipo acessorio.'''
    def __init__(self, nome, codigo_barras, categoria, quantidade, tipo_acessorio, produto_id = None, acessorio_id = None):
        super().__init__(nome, codigo_barras, categoria, quantidade, produto_id)
        self.tipo_acessorio = tipo_acessorio
        self.acessorio_id = acessorio_id

    def __str__(self):
        return f"ID do acessorio: {self.acessorio_id}\nID de produto desse acessorio: {self.produto_id}\nTipo do acessorio: {self.tipo_acessorio}"