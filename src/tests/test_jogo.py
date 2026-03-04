import pytest
from unittest.mock import patch
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.modules.domain.jogos import Jogo
from src.board_and_play_poo.modules.domain.produtos import Produto
from src.board_and_play_poo.repositories.repository_jogo import Repository_jogo
from src.board_and_play_poo.repositories.repository_produto import Repository_produto

# ------------------Testes de Repository------------------

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test
jogo_repo = Repository_jogo(db, tb)
produto_repo = Repository_produto(db, tb)

def teste_jogo_create():
    '''Teste para o método create de jogo repository'''
    # NECESSÁRIO CHECKS PARA CREATE EM APLICAÇÃO, como a tabela produto não tem mais uniques além do id ela pode se repetir com os mesmos dados, não tenho certeza o quanto isso poderia ser um problema em um caso real, porém é um bom assunto para discussão futura
    jogo = Jogo("WAR", "WAR-7196", "jogo", "estratégia", "É war, não tem segredo", 12, 4, 1)
    tupla = (jogo.nome, jogo.codigo_barras, jogo.categoria)
    jogo.produto_id = produto_repo.create(tupla)
    resultado = jogo_repo.create(jogo)
    assert resultado == "Jogo cadastrado"

#    (produto_id, genero, descricao, idade_min, num_jogadores)
           # VALUES (:produto_id, :genero, :descricao, :idade_min, :num_jogadores)

        # nome, codigo_barras, categoria, genero, descricao, idade_min, num_jogadores, produto_id = None, jogo_id=None

def teste_jogo_read():
    '''Teste para o método read de jogo repository'''
    jogo = jogo_repo.read(1)
    assert jogo.id == 1

def teste_jogo_update():
    '''Teste para o método update de jogo repository'''
    resultado = jogo_repo.update(1, "idade_min", 70)
    assert resultado == "Atributo atualizado"
