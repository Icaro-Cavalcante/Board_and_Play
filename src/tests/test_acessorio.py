import pytest
from unittest.mock import patch
from datetime import timedelta, date
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_acessorio import Repository_acessorio
from src.board_and_play_poo.modules.domain.acessorios import Acessorio

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
acessorio_repo = Repository_acessorio(db, tb)

def teste_acessorio_create():
    '''Teste para o método create de acessorio repository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    meses_2 = date.today() + timedelta(days=60)
    acessorio = Acessorio("chaveiro goku", "CHG-0987", "acessorio", 1, "chaveru", 4)
    resultado = acessorio_repo.create(acessorio)
    assert resultado == "Acessório cadastrado"

def teste_acessorio_read():
    '''Teste para o método read de acessorio repository'''
    acessorio = acessorio_repo.read(1)
    assert acessorio.id == 1

def teste_acessorio_update():
    '''Teste para o método update de acessorio repository'''
    resultado = acessorio_repo.update(1, "tipo_acessorio", "chaveiro")
    assert resultado == "Atributo atualizado"
