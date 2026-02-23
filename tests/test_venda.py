import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.services.venda import Venda
def teste_venda_create():
    '''Teste para o método create da classe venda.'''

    with patch('builtins.input', side_effect=["1" ,"1", "Jogo de tabuleiro"]):
        resultado = Venda.create()
        assert resultado == "Sucesso! Venda criada."

def teste_venda_read():
    '''Teste para o método read da classe venda.'''
    resultado = Venda.read(1)
    assert resultado[0] == 1
    
def teste_venda_update():
    '''Teste para o método update da classe venda.'''
    resultado = Venda.update(1, "tipo_produto", "Jogo de cartas")
    assert resultado == "Sucesso! Atributo atualizado."