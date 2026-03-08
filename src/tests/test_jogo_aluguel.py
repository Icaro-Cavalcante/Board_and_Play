import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.modules.domain.jogo_aluguel import JogoAluguel

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
j_aluguel_repo = RepositoryJogoAluguel(db, tb)

def teste_jogo_alugel_create():
    '''Teste para o método create da classe JogoAluguelRepository.'''
    jogo_aluguel = JogoAluguel("Monopoly", "PLO-9641", "jogo_aluguel", "Estratégia", "É war, não tem segredo", 12, 4, "HJH-8635" ,"DISPONIVEL", 1, 1)
    resultado = j_aluguel_repo.create(jogo_aluguel)
    assert resultado == "Jogo aluguel cadastrado"

def teste_jogo_aluguel_read():
    '''Teste para o método read da classe JogoAluguelRepository'''
    teste_jogo_alugel_create()
    resultado = j_aluguel_repo.read(1)
    assert resultado.categoria == "jogo_aluguel"

def teste_jogo_aluguel_update():
    '''Teste para o método update da classe JogoAluguelRepository'''
    teste_jogo_alugel_create()
    resultado = j_aluguel_repo.update(1, "nome", "War 2026")
    assert resultado == "Atributo atualizado."

def teste_jogo_aluguel_inactivate():
    '''Teste para o método inactivate da classe JogoAluguelRepository'''
    resultado = j_aluguel_repo.inactivate(1)
    assert resultado == "Jogo aluguel mudado para INATIVO com sucesso."
