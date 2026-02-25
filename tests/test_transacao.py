import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.services.transacoes import Transacao
from..src.board_and_play_poo.modules.services.aluguel import Aluguel
from..src.board_and_play_poo.modules.services.venda import Venda

def test_transacao_create_aluguel():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["1","1","2","3","pix","1","2"]):
        resultado = Transacao.create(aluguel)
        assert resultado == "\nComprovante criado.\n"

def test_transacao_read():
    resultado = Transacao.read(1)
    assert resultado == (1, 1, 300, 'pix', 400)

def test_transacao_tupla_objeto():
    resultado = Transacao.tupla_objeto(Transacao.read(1))
    print(resultado)
    assert resultado.metodo == 'pix'

def test_transacao_calcular_valor_aluguel_interno():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["2"]):
        interno = Transacao.calcular_valor(aluguel, 1)
    assert interno == 40   

def test_transacao_calcular_valor_aluguel_externo():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["2"]):
        externo = Transacao.calcular_valor(aluguel, 2)
    assert externo == 200

def test_transacao_calcular_valor_venda():
    venda = Venda.tupla_objeto(Venda.read(1))
    with patch('builtins.input', side_effect=["2"]):
        vender = Transacao.calcular_valor(venda, 3)
    assert vender == 200

def test_transacao_calcular_multa_aluguel():
    aluguel = Aluguel.tupla_objeto(Aluguel.read(1))
    with patch('builtins.input', side_effect=["1", "1"]):
        multa_v = Transacao.calcular_multa(aluguel)
    assert multa_v == 200

def test_transacao_calculcar_multa_venda():
    venda = Venda.tupla_objeto(Venda.read(1))
    multa_f = Transacao.calcular_multa(venda)
    assert multa_f == 0