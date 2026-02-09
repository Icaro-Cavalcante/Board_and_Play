from ..transacoes import Trans_venda
from .produtos import Produto
class Consumivel(Produto):
    '''Classe que cuida dos consumíveis (alimentos prontos, bebidas)'''
    def __init__(self, id, nome, qtd_compra, preco_total):
        super().__init__(id, nome, qtd_compra, preco_total)

    def criar():
        '''Cadastra um consumivel no banco de dados'''
        pass
    def ler(id):
        '''Recebe o id e retorna os dados do consumivel com esse id'''
        pass
    def editar():
        '''Edita os atributos de um consumivel no banco de dados'''
        pass
    def deletar():
        '''muda status para inativo'''
        pass