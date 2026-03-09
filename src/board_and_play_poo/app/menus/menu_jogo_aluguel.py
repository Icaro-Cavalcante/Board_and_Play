from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.modules.domain.jogo_aluguel import JogoAluguel
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db) # Criando tabelas do db de test

produto_repo = RepositoryProduto(db, tb)
jogo_repo = RepositoryJogo(db, tb)
jogo_aluguel_repo = RepositoryJogoAluguel(db, tb)

def decorator_cad_jogo_aluguel(func):
    """Como o menu chama o CREATE de um jogo_aluguel. Descreve o caminho I) Cria um Produto, II) Cria um Jogo, III) Cria um JogoAluguel"""
    def wrapper():
        lista = []
        lista.append(str(input(f"\nInsira o nome do produto: ")))
        lista.append(str(input(f"\nInsira o código de barras: ")))
        lista.append("JOGO")
        tupla = (lista)
        try:
            produto_id = produto_repo.create(tupla) # Passo I
        except TypeError:
            print("Dado inválido inserido, saindo do cadastro...")

        jogo_id = func(lista, produto_id)
        lista.append(str(input(f"\nInsira a etiqueta do jogo: ")))
        lista.append("DISPONIVEL")
        lista.append(produto_id)
        lista.append(jogo_id)
        jogo = JogoAluguel(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],lista[9], lista[10])
        jogo_aluguel_repo.create(jogo) # Passo III
        return "tristeza"
    return wrapper

@decorator_cad_jogo_aluguel # O decorator serve para definir a ordem de criação: primeiro cria um produto, passa o ID para criar um jogo, passa o ID para criar um jogo aluguel
def criar_jogo(lista, produto_id):
        gen = (str(input(f"\nInsira o gênero: ")))
        lista.append(gen)
        desc = (str(input(f"\nInsira a descrição: ")))
        lista.append(desc)
        while True:
            try:
                idade = (int(input(f"\nInsira a idade mínima: ")))
                lista.append(idade)
                break
            except ValueError:
                print("Dado inválido")
        num = (str(input(f"\nInsira o número de jogadores: ")))
        lista.append(num)
        tupla = (produto_id,gen,desc,idade,num)
        id = jogo_repo.create(tupla) # Passo II
        return id

def consultar():
    """Como o menu chama o READ de um JogoAluguel"""
    try:
        cont = int(input("\nDigite o id de um jogo alugável para busca: "))
        obj = jogo_aluguel_repo.read(cont)
        print(obj)
    except ValueError:
        print("\nDado inválido, saindo da consulta...\n")

def atualizar():
    """Como o menu chama o UPDATE de um JogoAluguel"""
    try:
        id = input("\nDigite o ID do jogo a ser alterado: ")
        nome_atributo = input("\nDigite o nome do atributo que deve ser alterado: ")
        novo_atributo = input("\nAtualizar para: ")
        jogo_aluguel_repo.update(id, nome_atributo, novo_atributo)
    except ValueError:
        print("\nDado inválido, saindo da atualização...\n")

class MenuJogoAluguel:
    def menu_jogo_aluguel(self):
        '''Menu da classe jogo aluguel'''
        while True:
            while True:
                try:
                    print("\nJogos alugáveis")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    criar_jogo()
                case 2:
                    consultar()
                case 3:
                    atualizar()
                case 4:
                    break
                case _:
                    print("Escolha inválida.\n")
a = MenuJogoAluguel()
a.menu_jogo_aluguel()