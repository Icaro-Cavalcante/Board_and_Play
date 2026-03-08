import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_jogo_venda import Repository_jogo_venda
from src.board_and_play_poo.modules.domain.jogos_venda import Jogo_venda

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
j_venda_repo = Repository_jogo_venda(db, tb)

def teste_jogo_venda_create():
    '''Teste para o método create da classe jogo venda repository.'''
    jogo_venda = Jogo_venda("Amigos", "QYI-8625", "jogo_venda", "Lúdico", "Game", 16, 2, 2, 2, 2)
    resultado = j_venda_repo.create(jogo_venda)
    assert resultado == "Jogo venda cadastrado"

def teste_jogo_venda_read():
    '''Teste para o método read da classe jogo venda repository.'''
    teste_jogo_venda_create()
    resultado = j_venda_repo.read(1)
    assert resultado.categoria == "jogo_venda"

def teste_jogo_venda_update():
    '''Teste para o método update da classe jogo venda repository.'''
    teste_jogo_venda_create()
    resultado = j_venda_repo.update(1, "nome", "Jogo dos amigos")
    assert resultado == "Atributo atualizado."