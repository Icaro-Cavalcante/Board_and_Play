"""
import pytest
from unittest.mock import patch
from datetime import timedelta, date
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_consumivel import Repository_consumivel
from src.board_and_play_poo.modules.domain.consumiveis import Consumivel

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
consumivel_repo = Repository_consumivel(db, tb)

def teste_consumivel_create():
    '''Teste para o método create de consumivel repository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    meses_2 = date.today() + timedelta(days=60)
    consumivel = Consumivel("coxinha", "COX-0987", "consumivel", 88908655409, meses_2, "lote", "GLUTEN", 3)
    resultado = consumivel_repo.create(consumivel)
    assert resultado == "Consumivel cadastrado"

def teste_consumivel_read():
    '''Teste para o método read de consumivel repository'''
    consumivel = consumivel_repo.read(1)
    assert consumivel.id == 1

def teste_consumivel_update():
    '''Teste para o método update de consumivel repository'''
    resultado = consumivel_repo.update(1, "lote", "AAAAA")
    assert resultado == "Atributo atualizado"

"""