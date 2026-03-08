from .transacoes import Transacao
from .clientes import Cliente
from .colaboradores import Colaborador

class Aluguel(Transacao):
    '''Classe responsável pelas transações de aluguel.'''
    def __init__(self, comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, numero_contrato, data_inicio, data_prevista_devolucao, data_devolucao_real, status, transacao_id=None, cliente_id=None, colaborador_id=None, aluguel_id=None):
        super().__init__(comprovante, data_hora, valor_total, forma_pagamento, tipo_transacao, transacao_id)
        self.numero_contrato = numero_contrato
        self.data_inicio = data_inicio
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao_real = data_devolucao_real
        self.status = status
        self.cliente_id = cliente_id
        self.colaborador_id = colaborador_id
        self.aluguel_id = aluguel_id

    def __str__(self):
        return f"ID do aluguel: {self.aluguel_id}\nID de transacao desse aluguel: {self.transacao_id}\nData inicio do aluguel: {self.data_inicio}\nData prevista para devolucao: {self.data_prevista_devolucao}\nData devolucao real: {self.data_devolucao_real}\n Status do aluguel: {self.status}\n ID do cliente desse aluguel: {self.cliente_id}\n ID do colaborador desse aluguel: {self.colaborador_id}"