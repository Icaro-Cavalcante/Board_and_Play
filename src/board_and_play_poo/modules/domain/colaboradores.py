class Colaborador:
    """
    Descreve os funcionários da loja e suas funções, como mediador, vendedor etc., mais seus turnos, dados pessoais, salário e status, serve para gerenciar as instâncias dos diversos colaboradores em suas aparições, como mediador em uma sessão de jogatina.
    """

    def __init__(self, cpf, nome, email, contato, contato_emergencia, salario, cargo, status, colaborador_id = None): # verificar se podemos encapsular esses atributos
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.contato = contato
        self.contato_emergencia = contato_emergencia
        self.salario = salario
        self.cargo = cargo
        self.status = status
        self.colaborador_id = colaborador_id

    def __str__(self):
        return f"ID do colaborador: {self.colaborador_id}\nCPF do colaborador: {self.cpf}\nNome do colaborador: {self.nome}\nE-mail do colaborador: {self.email}\nContato do colaborador: {self.contato}\nContato de emergência do colaborador: {self.colaborador}\nSalário base do colaborador: {self.salario}\nCargo do colaborador: {self.salario}\nStatus do colaborador: {self.status}"