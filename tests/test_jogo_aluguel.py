import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.domain.alugaveis import Jogo_aluguel

def teste_jogo_alugel_create():
    '''Teste para o método create da classe jogo aluguel.'''
    with patch('builtins.input', side_effect=["1","War","80.0","12/10/2025","Desafie seus amigos e descubra por que War é o jogo de estratégia mais jogado do Brasil!","10","3","tabuleiro","disponivel","20","40"]):
        resultado = Jogo_aluguel.create()

        assert resultado == "Sucesso! Jogo criado."

def teste_jogo_aluguel_read():
    '''Teste para o método read da classe jogo aluguel.'''
    resultado = Jogo_aluguel.read(1)
    assert resultado[0] == 1

def teste_jogo_aluguel_update():
    '''Teste para o método update da classe jogo aluguel.'''
    resultado = Jogo_aluguel.update(1, "valor_diaria", 100)
    assert resultado == "Sucesso! Atributo atualizado."

def teste_jogo_aluguel_delete():
    '''Teste para o método delete da classe jogo aluguel.'''
    resultado = Jogo_aluguel.delete(1)
    assert resultado == "Sucesso! Jogo inativado."

def teste_jogo_aluguel_tupla_objeto():
    '''Teste para o método tupla objeto da classe jogo aluguel.'''
    tupla = Jogo_aluguel.read(1)
    resultado = Jogo_aluguel.tupla_objeto(tupla)
    assert resultado._custo_aquisicao == 80
    