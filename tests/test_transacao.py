import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.services.transacoes import Transacao
from..src.board_and_play_poo.modules.services.aluguel import Aluguel

def test_transacao_create():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["1","1","1","1","pix"]):
        resultado = Transacao.create(aluguel)
        assert resultado == "\nComprovante criado.\n"

def test_transacao_create():
    resultado = Transacao.read(1)
    assert resultado == (1, 1, 1.0, 'pix', None)

def test_transacao_tupla_objeto():
    resultado = Transacao.tupla_objeto(Transacao.read(1))
    print(resultado)
    assert resultado.metodo == 'pix'

def test_transacao_calcular_valor():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["1","2"]):
        resultado = Transacao.calcular_valor(aluguel)
    assert resultado == 2

def test_transacao_calcular_multa():
    aluguel = Aluguel("1", "1", "1", "1", 1, 1)
    with patch('builtins.input', side_effect=["1"]):
        resultado = Transacao.calcular_multa(aluguel)
    assert resultado == 1