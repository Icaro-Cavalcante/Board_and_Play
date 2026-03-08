import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_jogo_aluguel import Repository_jogo_aluguel
from src.board_and_play_poo.modules.domain.jogo_aluguel import Jogo_aluguel

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
j_aluguel_repo = Repository_jogo_aluguel(db, tb)

def teste_jogo_alugel_create():
    '''Teste para o método create da classe jogo aluguel repository.'''
    jogo_aluguel = (1, "HGS7856", "ATIVO")
    resultado = j_aluguel_repo.create(jogo_aluguel)
    assert resultado == "Jogo aluguel cadastrado"

def teste_jogo_aluguel_read():
    '''Teste para o método read da classe jogo aluguel repository.'''
    teste_jogo_alugel_create()
    resultado = j_aluguel_repo.read(1)
    assert resultado.categoria == "jogo_aluguel"

def teste_jogo_aluguel_update():
    '''Teste para o método update da classe jogo aluguel repository.'''
    teste_jogo_alugel_create()
    resultado = j_aluguel_repo.update(1, "nome", "War 2026")
    assert resultado == "Atributo atualizado."

def teste_jogo_aluguel_inactivate():
    '''Teste para o método inactivate da classe jogo aluguel. repository'''
    resultado = j_aluguel_repo.inactivate(1)
    assert resultado == "Jogo aluguel mudado para INATIVO com sucesso."