"""import pytest
from unittest.mock import patch
#from..board_and_play_poo.modules.domain.compraveis import Jogo_venda

def teste_jogo_alugel_create():
    '''Teste para o método create da classe jogo aluguel.'''
    with patch('builtins.input', side_effect=["1","Banco imobiliario","80.0","12/10/2025","Se aventure nessa nova edição de Banco imobiliario","10","3","tabuleiro","disponivel","20"]):
        resultado = Jogo_venda.create()

        assert resultado == "Sucesso! Jogo criado."

def teste_jogo_aluguel_read():
    '''Teste para o método read da classe jogo aluguel.'''
    resultado = Jogo_venda.read(1)
    assert resultado[0] == 1

def teste_jogo_aluguel_update():
    '''Teste para o método update da classe jogo aluguel.'''
    resultado = Jogo_venda.update(1, "valor_compra", 100)
    assert resultado == "Sucesso! Atributo atualizado."

def teste_jogo_aluguel_delete():
    '''Teste para o método delete da classe jogo aluguel.'''
    resultado = Jogo_venda.delete(1)
    assert resultado == "Sucesso! Jogo inativado."

def teste_jogo_venda_tupla_objeto():
    '''Teste para o método tupla objeto da classe jogo venda.'''
    tupla = Jogo_venda.read(1)
    resultado = Jogo_venda.tupla_objeto(tupla)
    assert resultado._custo_aquisicao == 80
"""