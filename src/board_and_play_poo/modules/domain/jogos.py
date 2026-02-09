from .produtos import Produto

class Jogo(Produto):
    '''Descreve os atributos que existem em todas as especificações de jogos na loja, funciona como classe abstrata, a qual os atributos vão ser herdados pelas classes Jogo_aluguel e Jogo_venda.'''
    def __init__(self, id, nome, custo_aquisicao, data_aquisicao, descricao, idade_min, num_jogadores, tipo, status):
        super().__init__(id, nome, custo_aquisicao)
        self._descricao = descricao
        self._idade_min = idade_min
        self._data_aquisicao = data_aquisicao
        self._num_jogadores = num_jogadores
        self._status = status
        self._tipo = tipo