import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.venda import Venda
from src.board_and_play_poo.repositories.repository_venda import Repository_venda

tb = Tabela()
db = Database()
tb.create_test_table(db) # Criando tabelas do db de test
venda_repo = Repository_venda(db, tb)

# ------------------Testes de Repository------------------

def teste_venda_create():
    '''Teste para o método create da classe venda.'''
    venda = Venda(1, 1, 1, "nota")
    resultado = venda_repo.teste_create(venda)
    assert resultado == "Venda cadastrada."

def teste_venda_read():
    '''Teste para o método read da classe venda.'''
    teste_venda_create()
    resultado = venda_repo.teste_read(1)
    print(resultado)
    assert resultado.nota_fiscal == "nota"
    
def teste_venda_update():
    '''Teste para o método update da classe venda.'''
    teste_venda_create()
    resultado = venda_repo.teste_update(1, "colaboradores_id", 2)
    assert resultado == "Atributo atualizado."

"""def teste_venda_tupla_objeto():
    '''Teste para o método tupla objeto da classe venda.'''
    tupla = Venda.read(1)
    resultado = Venda.tupla_objeto(tupla)
    assert resultado.id_produto == 1"""

# ------------------Testes de Classe------------------
"""
def teste_venda_calcular_venda():
    '''Teste para o método tupla objeto da classe venda.'''
    tupla = Venda.read(1)
    objeto = Venda.tupla_objeto(tupla)
    resultado = objeto.calcular_venda(5)
    assert resultado == 5 * 100
"""