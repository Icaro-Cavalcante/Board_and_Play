import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.jogos import Jogo
from src.board_and_play_poo.repositories.repository_jogo import Repository_jogo

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database()
tb.create_test_table(db) # Criando tabelas do db de test
jogo_repo = Repository_jogo(db, tb)

def teste_jogo_create():
    '''Teste para o método create de jogo repository'''
    jogo = Jogo(1, "WAR-7196", "estratégia", "É war, não tem segredo", 44, 2, "ALUGAVEL", "DISPONIVEL")
    resultado = jogo_repo.teste_create(jogo)
    assert resultado == "Jogo cadastrado."

def teste_jogo_read():
    '''Teste para o método read de jogo repository'''
    teste_jogo_create()
    jogo = jogo_repo.teste_read(1)
    assert jogo.id == 1

def teste_jogo_update():
    '''Teste para o método update de jogo repository'''
    teste_jogo_create()
    resultado = jogo_repo.teste_update(1, "idade_min", 70)
    assert resultado == "Atributo atualizado."

def teste_jogo_inactivate():
    teste_jogo_create()
    resultado = jogo_repo.teste_inactivate(1)
    assert resultado == "Jogo inativado."
