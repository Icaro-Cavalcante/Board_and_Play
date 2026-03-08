from src.board_and_play_poo.modules.domain.jogos import Jogo

class JogoAluguel(Jogo):
    '''A classe dos jogos alugáveis'''
    def __init__(self, nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, etiqueta, status, produto_id = None, jogo_id=None, jogo_aluguel_id=None):
        super().__init__(nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id, jogo_id)
        self.__etiqueta = etiqueta
        self.__status = status
        self.__jogo_aluguel_id = jogo_aluguel_id
        
    @property
    def etiqueta(self):
        return self.__etiqueta
    
    @property
    def status(self):
        return self.__status
    
    @property
    def jogo_aluguel_id(self):
        return self.__jogo_aluguel_id

    @etiqueta.setter
    def etiqueta(self, novo_valor):
        self.__etiqueta = novo_valor

    @status.setter
    def status(self, novo_valor):
        self.__status = novo_valor

    @etiqueta.setter
    def jogo_aluguel_id(self, novo_valor):
        self.__jogo_aluguel_id = novo_valor