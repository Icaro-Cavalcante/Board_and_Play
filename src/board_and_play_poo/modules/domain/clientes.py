class Cliente:
    """
    Descreve o cliente que usufruirá dos serviços da loja, solicitando alugueis e compras. É usado para manter no histórico as ações de cada cliente, e seu status caso seja multado
    """

    def __init__(self, cpf, nome, email, contato, status, cliente_id = None): # verificar se podemos encapsular esses atributos
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.contato = contato
        self.status = status
        self.cliente_id = cliente_id

    def __str__(self):
        return f"ID do cliente: {self.cliente_id}\nCPF do cliente: {self.cpf}\nNome do cliente: {self.nome}\nE-mail do cliente: {self.email}\nContatos do cliente: {self.contato}\nStatus do cliente: {self.status}"