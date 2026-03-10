from src.board_and_play_poo.modules.domain.acessorios import Acessorio
from src.board_and_play_poo.repositories.repository_acessorio import RepositoryAcessorio
from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)

produto_repo = RepositoryProduto(db, tb)
acess_repo = RepositoryAcessorio(db, tb)

class MenuAcessorio:
    def menu_acessorio():
        '''Menu da classe acessorio'''
        while True:
            while True:
                try:
                    print("\nAcessorio")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuAcessorio.criar_acessorio()
                case 2:
                    MenuAcessorio.consultar()
                case 3:
                    MenuAcessorio.update()
                case 4:
                    break
                case _:
                    print("Escolha inválida.\n")

    def cadastro_acessorio(func):
        def wrapper():
            lista = []
            lista.append(str(input(f"\nInsira o nome do produto: ")))
            lista.append(str(input(f"\nInsira o código de barras: ")))
            lista.append("ACESSORIO")
            tupla = tuple(lista)
            try:
                produto_id = produto_repo.create(tupla) # Passo I
            except TypeError:
                print("Dado inválido inserido, saindo do cadastro...")
                return
            check = func(lista, produto_id)
            if check:
                print("Acessório cadastrado")
            else:
                print("Falha no cadastro, digite dados compatíveis com o cadastro")
        return wrapper

    @cadastro_acessorio
    def criar_acessorio(lista, prod_id):
        '''Cadastra um acessório no banco de dados'''
        while True:
            tipo = (str(input("Digite qual o tipo de acessório sendo cadastrado: ")))
            try:
                qtd = (int(input("Digite a quantia de acessórios para cadastro: ")))
                acess_obj = Acessorio(nome=lista[0], codigo_barras=lista[1], categoria=lista[2], tipo_acessorio=tipo, quantidade=qtd, produto_id=prod_id)
                acess_repo.create(acess_obj)
                return True
            except ValueError:
                print("Dado inválido inserido, retomando cadastro")

    def consultar():
        '''Chama o método READ de acessório'''
        while True:
            try:
                id = int(input("Insira o ID de um acessório: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        acessorio_consulta = acess_repo.read(id)
        if acessorio_consulta:
            dados = produto_repo.read(acessorio_consulta.produto_id)
            print(f"ID de produto: {dados[0]}\nCódigo de barras: {dados[1]}")
            acess_repo.imprimir_dados(acessorio_consulta)
        else:
            print("O acessório não existe no sistema")
    
    def update():
        """Como o menu chama o READ de um acessório"""
        while True:
            try:
                id = int(input("Insira o ID de um acessório: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        acessorio_consulta = acess_repo.read(id)
        if not acessorio_consulta:
            print("O acessório não existe.")
        else:
            """(self, nome, codigo_barras, categoria, tipo_acessorio, quantidade, produto_id = None, acessorio_id = None):"""
            dic_atributos = {1: "Nome", 2: "Codigo de barras", 3: "Tipo de acessório", 4: "Quantidade"}
            while True:
                try:
                    print("===Atributos===")
                    for atributo in dic_atributos:
                        print(f"{atributo} - {dic_atributos[atributo]}")
                    escolha = int(input("Escolha um atributo: "))
                    match escolha:
                        case 1 | 2 | 3:
                            update = str(input("Insira o dado atualizado: "))
                        case 4:
                            update = int(input("Insira o dado atualizado: "))
                        case _:
                            raise ValueError
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")
            nome_atributo = dic_atributos[escolha]
            acess_repo.update(id, nome_atributo, update)