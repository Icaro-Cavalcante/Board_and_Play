from .ativo import Ativo
from .transacao import Trans_ativo
class Carta(Ativo):
    '''Classe para a especificação de jogos (carta), descreve o tipo de jogo que é composto por um baralho, seja o tradicional ou outros tipos, como tarot(tipos de baralho) ou UNO(jogos específicos)'''
    def __init__(self, valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade, material, res_agua, profissional, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, esta_ativo = True):
        super().__init__(valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade,  id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, esta_ativo)
        self.__material__ = material
        self.res_agua = res_agua
        self.profissional = profissional

    def criar():
        '''Cadastra um jogo de cartas no banco de dados'''
        pass
    def ler(id):
        '''Recebe o id e retorna os dados do baralho com esse id'''
        pass
    def editar():
        '''Edita os atributos de um jogo de cartas no banco de dados'''
        pass
    def deletar():
        '''muda status para inativo'''
        pass