from src.board_and_play_poo.modules.domain.jogos import Jogo
class Jogo_venda(Jogo):
    '''A classe dos jogos compráveis'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, quantidade, produto_id = None, jogo_id=None, jogo_venda_id=None):
        super().__init__(nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id, jogo_id)
        self.__quantidade = quantidade
        self.__jogo_venda_id = jogo_venda_id
        
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def jogo_venda_id(self):
        return self.__jogo_venda_id

    @quantidade.setter
    def quantidade(self, novo_valor):
        self.__quantidade = novo_valor

    @jogo_venda_id.setter
    def jogo_venda_id(self, novo_valor):
        self.__jogo_venda_id = novo_valor
