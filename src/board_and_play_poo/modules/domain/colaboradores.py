class Colaborador:
    """
    Descreve os funcionários da loja e suas funções, como mediador, vendedor etc., mais seus turnos, dados pessoais, salário e status, serve para gerenciar as instâncias dos diversos colaboradores em suas aparições, como mediador em uma sessão de jogatina.
    """

    def __init__(self, cpf, nome, email, contato, contato_emergencia, salario, cargo, status, colaborador_id = None): # verificar se podemos encapsular esses atributos
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__contato = contato
        self.__contato_emergencia = contato_emergencia
        self.__salario = salario
        self.__cargo = cargo
        self.__status = status
        self.__colaborador_id = colaborador_id

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
    def contato_emergencia(self):
        return self.__contato_emergencia

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def status(self):
        return self.__status

    @property
    def colaborador_id(self):
        return self.__colaborador_id

    def __str__(self):
        return f"ID do colaborador: {self.__colaborador_id}\nCPF do colaborador: {self.__cpf}\nNome do colaborador: {self.__nome}\nE-mail do colaborador: {self.__email}\nContato do colaborador: {self.__contato}\nContato de emergência do colaborador: {self.__colaborador}\nSalário base do colaborador: {self.__salario}\nCargo do colaborador: {self.__salario}\nStatus do colaborador: {self.__status}"