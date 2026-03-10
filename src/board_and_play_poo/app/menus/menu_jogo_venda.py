from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo
from src.board_and_play_poo.repositories.repository_jogo_venda import RepositoryJogoVenda
from src.board_and_play_poo.modules.domain.jogos_venda import JogoVenda
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)

produto_repo = RepositoryProduto(db, tb)
jogo_repo = RepositoryJogo(db, tb)
jogo_venda_repo = RepositoryJogoVenda(db, tb)

def decorator_cad_jogo_venda(func):
    """Como o menu chama o CREATE de um jogo_venda. Descreve o caminho: I) Cria um Produto, II) Cria um Jogo, III) Cria um JogoVenda"""
    def wrapper():
        lista = []
        lista.append(str(input(f"\nInsira o nome do produto: ")))
        lista.append(str(input(f"\nInsira o código de barras: ")))
        lista.append("JOGO")
        tupla = tuple(lista)
        try:
            produto_id = produto_repo.create(tupla) # Passo I
        except TypeError:
            print("Dado inválido inserido, saindo do cadastro...")
            return

        jogo_id = func(lista, produto_id)
        lista.append(1)
        lista.append(produto_id)
        lista.append(jogo_id)
        jogo = JogoVenda(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],lista[9])
        jogo_venda_repo.create(jogo) # Passo III
        print("Jogo para venda cadastrado. Caso mais unidades devam entrar no sistema, atualize o atributo 'quantidade' deste jogo")
        return "alegria"
    return wrapper

@decorator_cad_jogo_venda # O decorator serve para definir a ordem de criação: primeiro cria um produto, passa o ID para criar um jogo, passa o ID para criar um jogo venda
def criar_jogo(lista, produto_id):
        '''Cria uma instância de jogo vendível no banco de dados'''
        while True:
            gen = (str(input(f"\nInsira o gênero: ")))
            lista.append(gen)
            desc = (str(input(f"\nInsira a descrição: ")))
            lista.append(desc)
            while True:
                try:
                    idade = (int(input(f"\nInsira a idade mínima: ")))
                    if idade <= 0:
                        raise ValueError
                    lista.append(idade)
                    num = (str(input(f"\nInsira o número de jogadores: ")))
                    lista.append(num)
                    tupla = (produto_id,gen,desc,idade,num)
                    id = jogo_repo.create(tupla) # Passo II
                    return id
                except ValueError:
                    print("Dado inválido, retomando cadastro")

def consultar():
    """Como o menu chama o READ de um JogoVenda"""
    while True:
        try:
            id = int(input("Insira o ID de um jogo: "))
            break
        except ValueError:
            print("\nTipo de dado inválido.\n")

    jogo_consulta = jogo_venda_repo.read(id)
    if not jogo_consulta:
        print("O jogo não existe.")
    else:
        dic_atributos = {1: "Nome", 2: "Codigo de barras", 3: "Código de barras", 4: "Genero", 5: "Descrição", 6: "Idade mínima", 7: "Número de jogadores", 8: "Quantidade"}
        while True:
            try:
                print("===Atributos===")
                for atributo in dic_atributos:
                    print(f"{atributo} - {dic_atributos[atributo]}")
                escolha = int(input("Escolha um atributo: "))
                match escolha:
                    case 1 | 2 | 3 | 4 | 5:
                        update = str(input("Insira o dado atualizado: "))
                    case 6 | 7 | 8:
                        update = int(input("Insira o dado atualizado: "))
                    case _:
                        raise ValueError
                break
            except ValueError:
                print("\nInput digitado não válido.\n")
        nome_atributo = dic_atributos[escolha]
        jogo_venda_repo.update(id, nome_atributo, update)

def atualizar():
    """Como o menu chama o UPDATE de um JogoVenda"""
    try:
        id = input("\nDigite o ID do jogo a ser alterado: ")
        nome_atributo = input("\nDigite o nome do atributo que deve ser alterado: ")
        novo_atributo = input("\nAtualizar para: ")
        jogo_venda_repo.update(id, nome_atributo, novo_atributo)
    except ValueError:
        print("\nDado inválido, saindo da atualização...\n")
        return

class MenuJogoVenda:
    def menu_jogo_venda():
        '''Menu da classe jogo venda'''
        while True:
            while True:
                try:
                    print("\nJogos para Venda")
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