from src.board_and_play_poo.repositories.repository_aluguel import RepositoryAluguel
from src.board_and_play_poo.repositories.repository_item_aluguel import RepositoryItemAluguel
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("teste")
tb.create_table(db) # Criando tabelas do db de test

aluguel_repo = RepositoryAluguel(db, tb)
item_repo = RepositoryItemAluguel(db, tb)

class MenuContrato:    
    def menu_contrato(self):
        '''Menu das consultas dos contratos de aluguel do sistema'''
        while True:
            while True:
                try:
                    print("\nContratos")
                    print("-" * 20)
                    print("1 - Consultar por ID\n2 - Consultar contratos abertos\n3 - Consultar contratos alterados\n4 - Consultar contratos fechados\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuContrato.menu_consultar_id()
                case 2:
                    MenuContrato.menu_consultar_status("ABERTO")
                case 3:
                    MenuContrato.menu_consultar_status("ALTERADO")
                case 4:
                    MenuContrato.menu_consultar_status("FECHADO")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_consultar_id():
        '''Menu para interagir com a função de consultar por id'''
        while True:
            try:
                id = int(input("Insira o id que deseja buscar: "))
                break
            except ValueError:
                print("\nId precisa ser um número inteiro!\n")
        contrato_consulta = aluguel_repo.read(id)
        if contrato_consulta:
            while True:
                while True:
                    try:
                        print(f"\nContrato {contrato_consulta.aluguel_id}")
                        print("-" * 20)
                        print("1 - Consultar atributos\n2 - Consultar itens\n3 - Sair")
                        escolha = int(input("Selecione uma opção: "))
                        break
                    except ValueError:
                        print("\nA opção deve ser um número inteiro.\n")
                match escolha:
                    case 1:
                        print(contrato_consulta)
                    case 2:
                        tuplas = item_repo.buscar_por_aluguel(contrato_consulta.aluguel_id)
                        for tupla in tuplas:
                            print("")
                            item_repo.imprimir_dados(tupla)
                            print("")
                    case 3:
                        break
                    case _:
                        print("Escolha inválida.\n")
        else:
            print("Não foi possível conectar")
            
    def menu_consultar_status(status):
        '''Menu para interagir com os contratos do status recebido'''
        contrato_consulta = (aluguel_repo.read_especifico(status))
        if contrato_consulta:
            for contrato in contrato_consulta:
                print("")
                print(contrato)
                print("")
        else:
            print("Não foi possível achar contratos.")