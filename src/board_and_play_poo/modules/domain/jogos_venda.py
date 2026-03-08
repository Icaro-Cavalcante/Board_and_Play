from src.board_and_play_poo.modules.domain.jogos import Jogo
class Jogo_venda(Jogo):
    '''A classe dos jogos compráveis'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, quantidade, produto_id = None, jogo_id=None, id=None):
        super().__init__(nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id, jogo_id)
        self.quantidade = quantidade
        self.id = id