"""import pytest
from unittest.mock import patch
from..board_and_play_poo.modules.domain.aluguel import Aluguel

# ------------------Testes de repository------------------

def teste_aluguel_create():
    '''Teste para o método create da classe aluguel.'''

    with patch('builtins.input', side_effect=["1", "1", "20/10/2025", "30/10/2025", "40", "100"]):
        resultado = Aluguel.create()
        assert resultado == "Sucesso! Aluguel criado."

def teste_aluguel_read():
    '''Teste para o método read da classe aluguel.'''
    resultado = Aluguel.read(1)
    assert resultado[0] == 1
    
def teste_aluguel_update():
    '''Teste para o método update da classe aluguel.'''
    resultado = Aluguel.update(1, "multa_diaria", 200)
    assert resultado == "Sucesso! Atributo atualizado."
"""

# ------------------Testes de classe------------------

"""
def teste_aluguel_calcular_multa():
    '''Teste para o método calcular multa da classe aluguel.'''
    obj_aluguel = Aluguel(1, 1, "20/10/2025", "30/10/2025", 40, 100)
    resultado = obj_aluguel.calcular_multa(5)
    assert resultado == 200

def teste_aluguel_calculo_aluguel_externo():
    '''Teste para o método calcular aluguel externo da classe aluguel.'''
    obj_aluguel = Aluguel(1, 1, "20/10/2025", "30/10/2025", 40, 100)
    resultado = obj_aluguel.calculo_aluguel_externo(5)
    assert resultado == 100 * 5

def teste_aluguel_calculo_aluguel_interno():
    '''Teste para o método calcular aluguel interno da classe aluguel.'''
    obj_aluguel = Aluguel(1, 1, "20/10/2025", "30/10/2025", 40, 100)
    resultado = obj_aluguel.calculo_aluguel_interno(5)
    assert resultado == 20 * 5

def teste_aluguel_tupla_objeto():
    '''Teste para o método tupla objeto da classe aluguel.'''
    tupla = Aluguel.read(1)
    resultado = Aluguel.tupla_objeto(tupla)
    assert resultado.multa_diaria == 200
"""