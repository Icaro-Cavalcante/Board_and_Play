import sqlite3
from abc import ABC, abstractmethod
from aluguel import Aluguel
from venda import Venda
from pathlib import Path
caminho_data = "src/board_and_play_poo/data/dados.db"

class Transacao(ABC):
    def __init__(self, id_transacao, id_cliente, id_colaborador, nota_fiscal):
        self._id_transacao = id_transacao
        self._id_cliente = id_cliente
        self._id_colaborador = id_colaborador
        self._nota_fiscal = nota_fiscal

    def __str__(self):
        return f"ID da transação: {self.id_transacao} | ID do cliente: {self._id_cliente} | ID do colaborador: {self._id_colaborador}\nNota fiscal: {self._nota_fiscal}\n"

    @abstractmethod
    def calcular_valor(self, obj_negocio):
        pass
        '''try:
            if obj_negocio.id_aluguel:
                escolha = int(input("\n1 - Aluguel interno\n2 - Aluguel externo"))
                match escolha:
                    case 1:
                        valor = Aluguel.calculo_aluguel_interno(int(input("\nDigite quantas sessões serão ofertadas: ")))
                    case 2:
                        valor = Aluguel.calculo_aluguel_externo(int(input("\nDigite a quantia de dias para locação: ")))
                    case _:
                        print("Escolha inválida, saindo de menu de cálculo.\n")
            elif obj_negocio.id_venda:
                valor = Venda.calcular_venda(int(input("Digite a quantia deste produto a ser comprado: ")))
        except AttributeError:
            return print("Tentativa de cálculo de valor falhou, tente repassar um aluguel/venda existente e ativo.")
        return valor'''

    @abstractmethod
    def calcular_multa(self, obj_negocio):
        pass
        '''try:
            if obj_negocio.id_venda:
                return 0
            elif obj_negocio.id_aluguel:
                valor = Aluguel.calcular_multa(int(input("Digite a quantia de dias além do prazo estipulado(0 se nenhum): ")))
        except AttributeError:
            return print("Tentativa de cálculo de multa falhou, tente repassar um aluguel existente e ativo.")
        return valor'''

