from src.board_and_play_poo.modules.domain.jogos import Jogo
class Jogo_aluguel(Jogo):
    '''A classe dos jogos alugáveis'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, etiqueta, status, produto_id = None, jogo_id=None, jogo_aluguel_id=None):
        super().__init__(nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id, jogo_id)
        self.etiqueta = etiqueta
        self.status = status
        self.jogo_aluguel_id = jogo_aluguel_id