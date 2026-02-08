from .produtos import Produto

class Jogo(Produto):
    '''Descreve os atributos e métodos gerais que existem em todas as especificações de jogos na loja, ajuda quanto ao controle de criação de instâncias e atributos em toda especificação.'''
    def __init__(self, id, nome, preco, descricao, categoria, idade_min, pub_recomendado, tipo, esta_ativo = True):
        super().__init__(id, nome, preco)
        self.__descricao = descricao
        self.__categoria = categoria
        self.__idade_min = idade_min
        self.__pub_recomendado = pub_recomendado
        self.__esta_ativo = esta_ativo
        self.__tipo = tipo

    def deletar():
            '''muda status para inativo'''
            pass