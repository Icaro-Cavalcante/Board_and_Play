from .ativo import Ativo
from .transacao import Trans_ativo
class Reliquia(Ativo):
    '''Descreve um jogo que não pode ser retirado da loja, só pode ser ultilizado dentro do local.'''
    def __init__(self, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado,valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade,tempo_h, tipo, esta_ativo = True):
        super().__init__(id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade, esta_ativo)
        self.__tempo_h__ = tempo_h
        self.__tipo__ = tipo

    def criar():
        '''Cadastra um jogo reliquia no banco de dados'''
        pass
    def ler(id):
        '''Recebe o id e retorna os dados do jogo reliquia com esse id'''
        pass
    def editar():
        '''Edita os atributos de um jogo reliquia no banco de dados'''
        pass
    def deletar():
        '''muda status para inativo'''
        pass