"""
import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.transacoes import Transacao
from src.board_and_play_poo.repositories.repository_transacao import Repository_transacao
# ------------------Testes de Repository------------------

tb = Tabela()
db = Database()
tb.create_test_table(db) # Criando tabelas do db de test
transacao_repo = Repository_transacao(db, tb)

def teste_transacao_create():
    '''Teste para o método create de transacao repository'''
    try:
        existe = transacao_repo.teste_read(1)
        if existe:
            resultado = "Transação cadastrada."
    except IndexError:
        transacao = Transacao("wtfever", 12, "PIX", "PENDENTE", "VENDA")
        resultado = transacao_repo.teste_create(transacao)
    assert resultado == "Transação cadastrada."

def teste_transacao_read():
    '''Teste para o método read de transacao repository'''
    transacao = transacao_repo.teste_read(1)
    assert transacao.id == 1

def teste_transacao_update():
    '''Teste para o método update de transacao repository'''
    resultado = transacao_repo.teste_update(1, "valor_total", 80)
    assert resultado == "Atributo atualizado."

def teste_transacao_inactivate():
    '''Teste para o método inactivate de transacao repository'''
    teste_transacao_create()
    resultado = transacao_repo.teste_inactivate(1)
    assert resultado == "Transação mudada para INATIVA com sucesso."

def teste_transacao_pagar():
    '''Teste para o método pagar de transacao repository'''
    resultado = transacao_repo.teste_pagar(1)
    assert resultado == "Pasagamento registrado com sucesso."
"""