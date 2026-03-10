from src.board_and_play_poo.repositories.repository_venda import RepositoryVenda
from src.board_and_play_poo.repositories.repository_item_venda import RepositoryItemVenda
from src.board_and_play_poo.repositories.repository_transacao import RepositoryTransacao
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)
venda_repo = RepositoryVenda(db, tb)
item_repo = RepositoryItemVenda(db, tb)
trans_repo = RepositoryTransacao(db, tb)

class MenuVenda:    
    def menu_venda():
        '''Menu das consultas das vendas do sistema'''
        while True:
            while True:
                try:
                    print("\nVendas")
                    print("-" * 20)
                    print("1 - Consultar por ID\n2 - Consultar por cliente\n3 - Consultar por método de pagamento\n4 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuVenda.busca_id()
                case 2:
                    MenuVenda.busca_geral("cliente_id", 1)
                case 3:
                    MenuVenda.busca_form()
                case 4:
                    break
                case _:
                    print("Escolha inválida.\n")
    def busca_id():
        '''Menu para interagir com a função de consultar por id'''
        while True:
            try:
                id = int(input("Insira o id que deseja buscar: "))
                break
            except ValueError:
                print("\nId precisa ser um número inteiro!\n")
        venda_consulta = venda_repo.read(id)
        if venda_consulta:
            while True:
                while True:
                    try:
                        print(f"\nVenda {venda_consulta.id}")
                        print("-" * 20)
                        print("1 - Consultar atributos\n2 - Consultar itens\n3 - Sair")
                        escolha = int(input("Selecione uma opção: "))
                        break
                    except ValueError:
                        print("\nA opção deve ser um número inteiro.\n")
                match escolha:
                    case 1:
                        print(venda_consulta)
                    case 2:
                        tuplas = item_repo.buscar_por_venda(venda_consulta.id)
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

    def busca_geral(atrb, inp):
        obj_lista = venda_repo.read_especifico(atrb, inp)
        for obj in obj_lista:
            print(obj)

    def busca_form():
        dic_atributos = {1: "PIX", 2: "Crédito", 3: "Débito", 4: "Dinheiro"}
        while True:
            try:
                print("===Atributos===")
                for atributo in dic_atributos:
                    print(f"{atributo} - {dic_atributos[atributo]}")
                escolha = int(input("Escolha um atributo: "))
                if escolha not in dic_atributos:
                    raise ValueError
                break
            except ValueError:
                print("\nInput digitado não válido.\n")
        form = dic_atributos[escolha]
        lista = trans_repo.read_especifico_join_venda("forma_pagamento", form)
        for tupla in lista:
            obj = venda_repo.tupla_objeto(tupla)
            print("\n", obj)