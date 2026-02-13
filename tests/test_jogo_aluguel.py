import pytest
from unittest.mock import patch
from..src.board_and_play_poo.modules.domain.alugaveis import Jogo_aluguel

def teste_alugel_create():
    '''Teste para o método create da classe jogo aluguel.'''
    with patch('builtins.input', side_effect=["1","War","80.0","12/10/2025","Desafie seus amigos e descubra por que War é o jogo de estratégia mais jogado do Brasil!","10","3","tabuleiro","disponivel","20","40"]):
        resultado = Jogo_aluguel.create()

        assert resultado == "Sucesso! Jogo criado."
