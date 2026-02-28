import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.produtos import Produto
from src.board_and_play_poo.repositories.repository_produto import Repository_produto

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database()
tb.create_test_table(db) # Criando tabelas do db de test
produto_repo = Repository_produto(db, tb)

def teste_produto_create():
    '''Teste para o método create de produto repository'''
    produto = Produto("AGT-7196", "War", 78.41, "12/10/2025", "jogo_aluguel", 12)
    resultado = produto_repo.teste_create(produto)
    assert resultado == "Jogo cadastrado."

def teste_produto_read():
    '''Teste para o método read de produto repository'''
    teste_produto_create()
    produto = produto_repo.teste_read(1)
    assert produto.id == 1

def teste_produto_update():
    '''Teste para o método update de produto repository'''
    teste_produto_create()
    resultado = produto_repo.teste_update(1, "custo_aquisicao", 80)
    assert resultado == "Atributo atualizado."
