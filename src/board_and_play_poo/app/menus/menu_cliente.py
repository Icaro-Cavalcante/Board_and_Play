from src.board_and_play_poo.repositories.repository_cliente import RepositoryCliente
from src.board_and_play_poo.modules.domain.clientes import Cliente
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db) # Criando tabelas do db de test

cliente_repo = RepositoryCliente(db, tb)


class MenuCliente:
    def menu_cliente():
        '''Menu da classe cliente'''
        while True:
            while True:
                try:
                    print("\nClientes")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Inativar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuCliente.cadastro()
                case 2:
                    MenuCliente.consultar()
                case 3:
                    MenuCliente.atualizar_dados()
                case 4:
                    MenuCliente.menu_inativar()
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def cadastro():
        '''Função de cadastro do menu'''
        while True:
            try:
                cpf = str(input("Insira o CPF: "))
                nome = str(input("Insira o nome: "))
                email = str(input("Insira o email: "))
                contato = str(input("Insira o contato: "))
                status = str(input("Insira o status: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")
        novo_cliente = Cliente(cpf, nome, email, contato, status)
        cliente_repo.create(novo_cliente)
        print("Cliente cadastrado com sucesso!")

    def consultar():
        '''Menu para consultar os dados de um cliente caso ele exista'''
        while True:
            try:
                id = int(input("Insira o ID de um cliente: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        cliente_consulta = cliente_repo.read(id)
        if cliente_consulta:
            cliente_repo.imprimir_dados(cliente_consulta)
        else:
            print("O cliente não existe.")

    def atualizar_dados():
        '''Menu para atualizar dados do cliente'''
        while True:
            try:
                id = int(input("Insira o ID de um cliente: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        cliente_consulta = cliente_repo.read(id)
        if not cliente_consulta:
            print("O cliente não existe.")
        else:
            dic_atributos = {1: "CPF", 2: "Nome", 3: "Email", 4: "Contato", 5: "Status"}
            while True:
                try:
                    print("===Atributos===")
                    for atributo in dic_atributos:
                        print(f"{atributo} - {dic_atributos[atributo]}")
                    escolha = int(input("Escolha um atributo: "))
                    if escolha not in dic_atributos:
                        raise ValueError
                    update = str(input("Insira o dado atualizado: "))
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")
            nome_atributo = dic_atributos[escolha]
            cliente_repo.update(id, nome_atributo, update)
            print("Atributo atualizado com sucesso!")

    def menu_inativar():
        '''Menu de inativar um cliente'''
        while True:
            try:
                id = int(input("Insira o ID de um cliente: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        cliente_consulta = cliente_repo.read(id)
        if not cliente_consulta:
            print("O cliente não existe.")
        else:
            while True:
                try:
                    print("\nCliente encontrado deseja inativá-lo?\n1 - Sim\n2 - Não")
                    escolha = int(input("Sua escolha: "))
                    match escolha:
                        case 1:
                            cliente_repo.inactivate(id)
                            print("Cliente inativado com sucesso!")
                        case 2:
                            break
                        case _:
                            raise ValueError
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")