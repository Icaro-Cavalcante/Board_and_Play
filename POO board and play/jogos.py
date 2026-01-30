class Jogo:
    '''Descreve os atributos e métodos gerais que existem em todas as especificações de jogos na loja, ajuda quanto ao controle de criação de instâncias e atributos em toda especificação.'''
    def __init__(self, id, nome, descricao, categoria, qtd_jogadores, idade_min, qtd_total, pub_recomendado, esta_ativo = True):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__categoria = categoria
        self.__qtd_jogadores = qtd_jogadores
        self.__idade_min = idade_min
        self.__qtd_total = qtd_total
        self.__pub_recomendado = pub_recomendado
        self.__esta_ativo = esta_ativo

    def deletar():
            '''muda status para inativo'''
            pass