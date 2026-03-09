from .transacoes import Transacao
from .clientes import Cliente
from .colaboradores import Colaborador
from board_and_play_poo.modules.infrastructure.descontos import DescontoPorcent, DescontoValorFixo

class Aluguel():
    '''Classe responsável pelas transações de aluguel'''
    def __init__(self, numero_contrato, data_inicio, data_prevista_devolucao, data_devolucao_real, status, cliente_id=None, colaborador_id=None, transacao_id=None, aluguel_id=None):
        self.__numero_contrato = numero_contrato
        self.__data_inicio = data_inicio
        self.__data_prevista_devolucao = data_prevista_devolucao
        self.__data_devolucao_real = data_devolucao_real
        self.__status = status
        self.__transacao_id = transacao_id
        self.__cliente_id = cliente_id
        self.__colaborador_id = colaborador_id
        self.__aluguel_id = aluguel_id

    @property
    def numero_contrato(self):
        return self.__numero_contrato

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_prevista_devolucao(self):
        return self.__data_prevista_devolucao

    @property
    def data_devolucao_real(self):
        return self.__data_devolucao_real

    @property
    def status(self):
        return self.__status

    @property
    def cliente_id(self):
        return self.__cliente_id

    @property
    def colaborador_id(self):
        return self.__colaborador_id
        
    @property
    def transacao_id(self):
        return self.__transacao_id

    @property
    def aluguel_id(self):
        return self.__aluguel_id

    def __str__(self):
        return f"ID do aluguel: {self.__aluguel_id}\nID de transacao desse aluguel: {self.__transacao_id}\nData inicio do aluguel: {self.__data_inicio}\nData prevista para devolucao: {self.__data_prevista_devolucao}\nData devolucao real: {self.__data_devolucao_real}\n Status do aluguel: {self.__status}\n ID do cliente desse aluguel: {self.__cliente_id}\n ID do colaborador desse aluguel: {self.__colaborador_id}"
    
    def AplicarDesconto(self, valor: float, tipo: str):
        """Aplica desconto ao valor passado baseado no tipo, tipo deve ser ou 'porcentagem' ou 'valorfixo', não case sensitive"""
        if tipo.lower == "porcentagem":
            while True:
                try:
                    porcent = int(input("Digite a porcentagem do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoPorcent(porcent)
            valor = descont.AplicarDesconto(valor)
            return valor
        if tipo.lower == "valorfixo":
            while True:
                try:
                    vfixo = int(input("Digite o valor do desconto do desconto: "))
                    break
                except ValueError:
                    print("Dado inválido digitado.")
            descont = DescontoValorFixo(vfixo)
            valor = descont.AplicarDesconto(valor)
            return valor