from .produtos import Produto

class Alugavel(Produto):
    """Descreve a classe de itens alugáveis, definindo seus atributos e métodos semelhantes, sendo herdado em cada um 'reliquias, cartas e tabuleiros'"""
    def __init__(self, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, valor_aluguel, multa, qtd_disponivel, qtd_manutencao, reposicao, tempo_aluguel, complexidade, esta_ativo = True):
                super().__init__(id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, esta_ativo)
                self.__valor_aluguel = valor_aluguel
                self.__multa_ = multa
                self.__qtd_disponivel = qtd_disponivel
                self.__qtd_manutencao = qtd_manutencao
                self.__reposicao_ = reposicao
                self.__tempo_aluguel = tempo_aluguel
                self.__complexidade = complexidade

    def criar():
            '''cria instância, atribuindo seus dados nos atributos e seguindo em frente para classes filho'''
            pass
    def ler():
            '''mostra os dados cadastrados em relação a uma instância'''
            pass