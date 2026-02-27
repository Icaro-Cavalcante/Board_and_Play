class Produto:
    '''Integra atributos em comum de suas subclasses, mantendo controle do atributo 'custo' para verificar valor de operação/despesa'''

    def __init__(self, codigo_barras, nome, custo_aquisicao, data_aquisicao, categoria, quantidade, id=None): # O ID não deve ser passado como parâmetro
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.custo_aquisicao = custo_aquisicao
        self.data_aquisicao = data_aquisicao
        self.categoria = categoria
        self.quantidade = quantidade
        self.id = id


    def __str__(self):
        return f"ID do produto: {self.id} | Código de barras do produto: {self.codigo_barras} | Nome do produto: {self.nome}\nCusto de aquisição do produto: {self.custo_aquisicao} | Data de aquisição do produto: {self.data_aquisicao} | Categoria do produto: {self.categoria}\n Quantidade disponível do produto: {self.quantidade}."