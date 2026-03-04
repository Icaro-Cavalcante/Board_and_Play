from .produtos import Produto

class Jogo(Produto):
    '''Descreve os atributos que existem em todas as especificações de jogos.'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id = None, jogo_id=None):
        super().__init__(nome, codigo_barras, categoria, produto_id)
        self.genero = genero
        self.descricao = descricao
        self.idade_min = idade_min
        self.num_jogadores = num_jogadores
        self.jogo_id = jogo_id