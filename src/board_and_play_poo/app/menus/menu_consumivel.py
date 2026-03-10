from src.board_and_play_poo.modules.domain.consumiveis import Consumivel
from src.board_and_play_poo.repositories.repository_consumivel import RepositoryConsumivel
from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)

produto_repo = RepositoryProduto(db, tb)
consumivel_repo = RepositoryConsumivel(db, tb)

class MenuConsumivel:
    def menu_consumivel():
        '''Menu da classe consumivel'''
        while True:
            while True:
                try:
                    print("\nConsumíveis")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuConsumivel.criar_consumivel()
                case 2:
                    MenuConsumivel.consultar()
                case 3:
                    MenuConsumivel.update()
                case 4:
                    break
                case _:
                    print("Escolha inválida.\n")

    def cadastro_consumivel(func):
        def wrapper():
            lista = []
            lista.append(str(input(f"\nInsira o nome do produto: ")))
            lista.append(str(input(f"\nInsira o código de barras: ")))
            lista.append("CONSUMIVEL")
            tupla = tuple(lista)
            try:
                produto_id = produto_repo.create(tupla) # Passo I
            except TypeError:
                print("Dado inválido inserido, saindo do cadastro...")
                return
            check = func(lista, produto_id)
            if check:
                print("Consumível cadastrado")
            else:
                print("Falha no cadastro, digite dados compatíveis com o cadastro")
        return wrapper

    @cadastro_consumivel
    def criar_consumivel(lista, prod_id):
        '''Cadastra um consumível no banco de dados'''
        while True:
            data_validade = (str(input("Digite a data de validade (DD/MM/YYYY): ")))
            lote = (str(input("Digite o lote do produto: ")))
            restricoes = (str(input("Digite as restrições (alergênios, etc): ")))
            try:
                qtd = (int(input("Digite a quantia de consumíveis para cadastro: ")))
                consumivel_obj = Consumivel(nome=lista[0], codigo_barras=lista[1], categoria=lista[2], data_validade=data_validade, lote=lote, restricoes=restricoes, quantidade=qtd, produto_id=prod_id)
                consumivel_repo.create(consumivel_obj)
                return True
            except ValueError:
                print("Dado inválido inserido, retomando cadastro")

    def consultar():
        '''Chama o método READ de consumível'''
        while True:
            try:
                id = int(input("Insira o ID de um consumível: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        consumivel_consulta = consumivel_repo.read(id)
        if consumivel_consulta:
            dados = produto_repo.read(consumivel_consulta.produto_id)
            print(f"ID de produto: {dados[0]}\nCódigo de barras: {dados[1]}")
            print(f"ID do consumível: {consumivel_consulta[0]}\nID de produto: {consumivel_consulta[1]}\nData de validade: {consumivel_consulta[2]}\nLote: {consumivel_consulta[3]}\nRestrições: {consumivel_consulta[4]}\nQuantidade: {consumivel_consulta[5]}")
        else:
            print("O consumível não existe no sistema")
    
    def update():
        """Atualiza um consumível"""
        while True:
            try:
                id = int(input("Insira o ID de um consumível: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        consumivel_consulta = consumivel_repo.read(id)
        if not consumivel_consulta:
            print("O consumível não existe.")
        else:
            dic_atributos = {1: "data_validade", 2: "lote", 3: "restricoes", 4: "quantidade"}
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
            consumivel_repo.update(id, nome_atributo, update)