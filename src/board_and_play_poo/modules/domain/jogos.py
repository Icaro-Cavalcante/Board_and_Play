class Jogo():
    '''Descreve os atributos que existem em todas as especificações de jogos.'''
    def __init__(self, produto_id, etiqueta, genero, descricao, idade_min, num_jogadores, tipo_jogo, status, id=None):
        self.produto_id = produto_id
        self.etiqueta = etiqueta
        self.genero = genero
        self.descricao = descricao
        self.idade_min = idade_min
        self.num_jogadores = num_jogadores
        self.tipo_jogo = tipo_jogo
        self.status = status
        self.id = id

    def __str__(self):
        return f"ID do jogo: {self.id}\nID de produto desse jogo: {self.produto_id}\nEtiqueta: {self.etiqueta}\nGênero do jogo: {self.genero}\nDescrição: {self.descricao}\nIdade mínima: {self.idade_min}\nNúmero mínimo de jogadores: {self.num_jogadores}\nTipo do jogo: {self.tipo_jogo}\nStatus: {self.status}"