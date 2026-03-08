from .produtos import Produto

class Jogo(Produto):
    '''Descreve os atributos que existem em todas as especificações de jogos.'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id = None, jogo_id=None):
        super().__init__(nome, codigo_barras, categoria, produto_id)
        self._genero = genero
        self._descricao = descricao
        self._idade_min = idade_min
        self._num_jogadores = num_jogadores
        self._jogo_id = jogo_id

    @property
    def genero(self):
        return self._genero

    @property
    def descricao(self):
        return self._descricao
    
    @property
    def idade_min(self):
        return self._idade_min
    
    @property
    def num_jogadores(self):
        return self._num_jogadores
    
    @property
    def jogo_id(self):
        return self._jogo_id

    @genero.setter
    def genero(self, novo_valor):
        self._genero = novo_valor

    @descricao.setter
    def descricao(self, novo_valor):
        self._descricao = novo_valor

    @idade_min.setter
    def idade_min(self, novo_valor):
        self._idade_min = novo_valor

    @num_jogadores.setter
    def num_jogadores(self, novo_valor):
        self._num_jogadores = novo_valor

    @jogo_id.setter
    def jogo_id(self, novo_valor):
        self._jogo_id = novo_valor
