from .ativo import Ativo
from .transacao import Trans_ativo
class Tabuleiro(Ativo):

    '''Descreve os atributos e métodos de jogos de tabuleiro, levando em conta variáveis que influenciam no preço de aluguel e multa, e a presença de um mediador.'''

    def __init__(self, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado,valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade,qtd_pecas, lista_pecas, tempo_medio, risco_perda_pecas, mediador = False, esta_ativo = True):
        super().__init__(id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado,valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade, esta_ativo)
        self.__qtd_pecas = qtd_pecas
        self.__lista_pecas = lista_pecas
        self.__tempo_medio = tempo_medio
        self.__risco_perda_pecas = risco_perda_pecas
        self.__mediador = mediador

    def criar():
        '''Cadastra um jogo de tabuleiro no banco de dados'''
        pass
    def ler(id):
        '''Recebe o id e retorna os dados do tabuleiro com esse id'''
        pass
    def editar():
        '''Edita os atributos de um jogo de tabuleiro no banco de dados'''
        pass
    def deletar():
        '''muda status para inativo'''
        pass