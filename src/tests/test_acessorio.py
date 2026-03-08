import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_acessorio import RepositoryAcessorio
from src.board_and_play_poo.modules.domain.acessorios import Acessorio

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
acessorio_repo = RepositoryAcessorio(db, tb)

def teste_acessorio_create():
    '''Teste para o método create de AcessorioRepository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    acessorio = Acessorio("chaveiro goku", "CHG-0987", "acessorio", 1, "chaveru", 4)
    resultado = acessorio_repo.create(acessorio)
    assert resultado == "Acessório cadastrado"

def teste_acessorio_read():
    '''Teste para o método read de AcessorioRepository'''
    acessorio = acessorio_repo.read(1)
    assert acessorio.id == 1

def teste_acessorio_update():
    '''Teste para o método update de AcessorioRepository'''
    resultado = acessorio_repo.update(1, "tipo_acessorio", "chaveiro")
    assert resultado == "Atributo atualizado"
