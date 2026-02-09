class Cliente:

    """Descreve o cliente que usufruirá dos serviços da loja, solicitando alugueis e compras. É usado para manter no histórico as ações de cada cliente, e seu status caso seja multado"""


    def __init__(self, cpf, email, item_atual, multa_pend, nome, disponivel = True):
        #historio?
        self.__cpf = cpf
        self.__email = email
        self.item_atual = item_atual
        self.multa_pend = multa_pend
        self.__nome = nome
        self.disponivel = disponivel

    def criar():
        '''cria uma instância de cliente no banco de dados'''
        pass
    def ler():
        '''permite a visualização dos dados de ums instância de cliente'''
        pass
    def deletar():
        '''muda status pra inativo'''