class Cliente:
    """Descreve o cliente que usufruirá dos serviços da loja, solicitando alugueis e compras. É usado para manter no histórico as ações de cada cliente, e seu status caso seja multado"""

    def __init__(self, cpf, nome, email, contato, status, cliente_id = None): # verificar se podemos encapsular esses atributos
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__contato = contato
        self.__status = status
        self.__cliente_id = cliente_id

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def contato(self):
        return self.__contato

    @property
    def status(self):
        return self.__status

    @property
    def cliente_id(self):
        return self.__cliente_id

    def __str__(self):
        return f"ID do cliente: {self.__cliente_id} | CPF do cliente: {self.__cpf} | Nome do cliente: {self.__nome}\nE-mail do cliente: {self.__email} | Contatos do cliente: {self.__contato} | Status do cliente: {self.__status}"