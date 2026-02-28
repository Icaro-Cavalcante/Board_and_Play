import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.produtos import Produto
from src.board_and_play_poo.repositories.repository_produto import Repository_produto

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
produto_repo = Repository_produto(db, tb)

def teste_produto_create():
    '''Teste para o método create de produto repository'''
    produto = Produto("PLO-9641", "Monopoly", 78.41, "12/10/2025", "jogo_aluguel", 12)
    resultado = produto_repo.create(produto)
    assert resultado == "Jogo cadastrado."

def teste_produto_read():
    '''Teste para o método read de produto repository'''
    teste_produto_create()
    produto = produto_repo.read(1)
    assert produto.id == 1

def teste_produto_update():
    '''Teste para o método update de produto repository'''
    teste_produto_create()
    resultado = produto_repo.update(1, "custo_aquisicao", 80)
    assert resultado == "Atributo atualizado."
