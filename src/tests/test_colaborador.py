import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_colaborador import Repository_colaborador
from src.board_and_play_poo.modules.domain.colaboradores import Colaborador

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
colaborador_repo = Repository_colaborador(db, tb)

def teste_colaborador_create():
    '''Teste para o método create de colaborador repository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    colaborador = Colaborador("12345678-09", "Júlio César", "peneira1@yahoo.com", "88908655409", "90876543212", 0.00, "Estagirátio", "àPostos :)")
    resultado = colaborador_repo.create(colaborador)
    assert resultado == "Colaborador cadastrado"

def teste_colaborador_read():
    '''Teste para o método read de colaborador repository'''
    colaborador = colaborador_repo.read(1)
    assert colaborador.id == 1

def teste_colaborador_update():
    '''Teste para o método update de colaborador repository'''
    resultado = colaborador_repo.update(1, "salario", 10)
    assert resultado == "Atributo atualizado"

def teste_colaborador_inactivate():
    resultado = colaborador_repo.inactivate(1)
    assert resultado == "Colaborador inativado"
