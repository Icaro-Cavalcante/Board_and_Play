class Produto:
    '''Integra atributos em comum de suas subclasses, mantendo controle do atributo 'custo' para verificar valor de operação/despesa'''

    def __init__(self, codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria, id=None): # O ID não deve ser passado como parâmetro
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.custo_aquisicao = custo_aquisicao
        self.data_aquisicao = data_aquisicao
        self.categoria = categoria
        self.id = id