class Colaborador:

    """Descreve os funcionários da loja e suas funções, como mediador, vendedor etc., mais seus turnos, dados pessoais, salário e status, serve para gerenciar as instâncias dos diversos colaboradores em suas aparições, como mediador em uma sessão de jogatina."""

    def __init__(self, cpf, nome, salario, tipo, status, turno):
        self.__cpf__ = cpf
        self.__nome__ = nome
        self.__salario__ = salario
        self.__tipo__ = tipo
        self.status = status
        self.__turno__ = turno