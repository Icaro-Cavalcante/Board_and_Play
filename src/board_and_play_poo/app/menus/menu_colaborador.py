from src.board_and_play_poo.repositories.repository_colaborador import RepositoryColaborador
from src.board_and_play_poo.modules.domain.colaboradores import Colaborador
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db) # Criando tabelas do db de test

colaborador_repo = RepositoryColaborador(db, tb)


class MenuColaborador:
    def menu_colaborador():
        '''Menu da classe colaborador'''
        while True:
            while True:
                try:
                    print("\nColaboradores")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Desligar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuColaborador.cadastro()
                case 2:
                    MenuColaborador.consultar()
                case 3:
                    MenuColaborador.atualizar_dados()
                case 4:
                    MenuColaborador.menu_desligar()
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
                contato_emergencia = str(input("Insira o contato_emergencia: "))
                salario = float(input("Insira o salario: "))
                cargo = str(input("Insira o cargo: "))
                status = str(input("Insira o status: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")    
        novo_colaborador = Colaborador(cpf, nome, email, contato, contato_emergencia, salario, cargo, status)
        colaborador_repo.create(novo_colaborador)

    def consultar():
        '''Menu para onsultar os dados de um colaborador caso ele exista'''
        while True:
            try:
                id = int(input("Insira o ID de um colaborador: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        colaborador_consulta = colaborador_repo.read(id)
        if colaborador_consulta:
            print(colaborador_consulta)
        else:
            print("O colaborador não existe.")

    def atualizar_dados():
        '''Menu para atualizar dados do colaborador'''
        while True:
            try:
                id = int(input("Insira o ID de um colaborador: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        colaborador_consulta = colaborador_repo.read(id)
        if not colaborador_consulta:
            print("O colaborador não existe.")
        else:
            dic_atributos = {1: "CPF", 2: "Nome", 3: "Email", 4: "Contato", 5: "Contato de emergencia", 6: "Salário", 7: "Cargo", 8: "Status"}
            while True:
                try:
                    print("===Atributos===")
                    for atributo in dic_atributos:
                        print(f"{atributo} - {dic_atributos[atributo]}")
                        escolha = int(input("Escolha um atributo: "))
                        match escolha:
                            case 1 | 2 | 3 | 4 | 5 | 7 | 8:
                                update = str(input("Insira o dado atualizado: "))
                            case 6:
                                update = float(input("Insira o dado atualizado: "))
                            case _:
                                raise ValueError
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")
            nome_atributo = dic_atributos[escolha]
            colaborador_repo.update(id, nome_atributo, update)

    def menu_desligar():
        '''Menu de desligar um colaborador'''
        while True:
            try:
                id = int(input("Insira o ID de um colaborador: "))
                break
            except ValueError:
                print("\nTipo de dado inválido.\n")

        colaborador_consulta = colaborador_repo.read(id)
        if not colaborador_consulta:
            print("O colaborador não existe.")
        else:
            while True:
                try:
                    print("\nColaborador encontrado deseja desligá-lo?\n1 - Sim\n2 - Não")
                    escolha = int(input("Sua escolha: "))
                    match escolha:
                        case 1:
                            colaborador_repo.inactivate(id)
                        case 2:
                            break
                        case _:
                            raise ValueError
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")