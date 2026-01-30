from .jogos import Jogo
from .transacao import Trans_venda
class Produto(Jogo):
    '''Descreve um jogo que não é alugado, será vendido como produto.'''

    def __init__(self, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado,preco, tipo, esta_ativo = True):
        super().__init__(id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, esta_ativo)
        self.__preco__ = preco
        self.__tipo__ = tipo