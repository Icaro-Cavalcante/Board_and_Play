import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
jogo_repo = RepositoryJogo(db, tb)

def teste_jogo_create():
    '''Teste para o método create de JogoRepository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    jogo = (1, "Estratégia", "É war, não tem segredo", 12, 4)
    jogo2 = (2, "Lúdico", "Game", 16, 2)
    resultado = jogo_repo.create(jogo)
    jogo_repo.create(jogo2)
    assert resultado == "Jogo cadastrado"

def teste_jogo_read():
    '''Teste para o método read de JogoRepository'''
    jogo = jogo_repo.read(1)
    assert jogo[0] == 1

def teste_jogo_update():
    '''Teste para o método update de JogoRepository'''
    resultado = jogo_repo.update(1, "idade_min", 70)
    assert resultado == "Atributo atualizado"
