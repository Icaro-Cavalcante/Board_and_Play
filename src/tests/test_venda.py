import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.domain.venda import Venda
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

def teste_venda_tupla_objeto():
    '''Teste para o método tupla objeto da classe venda.'''
    tupla = Venda.read(1)
    resultado = Venda.tupla_objeto(tupla)
    assert resultado.id_produto == 1

def teste_venda_calcular_venda():
    '''Teste para o método tupla objeto da classe venda.'''
    tupla = Venda.read(1)
    objeto = Venda.tupla_objeto(tupla)
    resultado = objeto.calcular_venda(5)
    assert resultado == 5 * 100