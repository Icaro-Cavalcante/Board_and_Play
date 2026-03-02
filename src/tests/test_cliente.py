import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_cliente import Repository_cliente
from src.board_and_play_poo.modules.domain.clientes import Cliente

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
cliente_repo = Repository_cliente(db, tb)

def teste_cliente_create():
    '''Teste para o método create de cliente repository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    cliente = Cliente("12345678-09", "Rick", "nggyu@gmail.com", "88908655409", "ATIVO")
    resultado = cliente_repo.create(cliente)
    assert resultado == "Cliente cadastrado"

def teste_cliente_read():
    '''Teste para o método read de cliente repository'''
    cliente = cliente_repo.read(1)
    assert cliente.id == 1

def teste_cliente_update():
    '''Teste para o método update de cliente repository'''
    resultado = cliente_repo.update(1, "status", "MULTADO")
    assert resultado == "Atributo atualizado"

def teste_cliente_inactivate():
    resultado = cliente_repo.inactivate(1)
    assert resultado == "Cliente inativado"
