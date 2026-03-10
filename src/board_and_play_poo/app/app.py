from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_aluguel import RepositoryAluguel
from src.board_and_play_poo.repositories.repository_item_aluguel import RepositoryItemAluguel
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.app.menus.menu_acessorio import MenuAcessorio
from src.board_and_play_poo.app.menus.menu_cliente import MenuCliente
from src.board_and_play_poo.app.menus.menu_colaborador import MenuColaborador
from src.board_and_play_poo.app.menus.menu_consumivel import MenuConsumivel
from src.board_and_play_poo.app.menus.menu_contrato import MenuContrato
from src.board_and_play_poo.app.menus.menu_jogo_aluguel import MenuJogoAluguel
from src.board_and_play_poo.app.menus.menu_jogo_venda import MenuJogoVenda
from src.board_and_play_poo.app.menus.menu_registrar_venda import MenuRegistrarVenda
from src.board_and_play_poo.app.menus.menu_venda import MenuVenda
from src.board_and_play_poo.services.service_aluguel import ServiceAluguel
from src.board_and_play_poo.app.menus.menu_registrar_contrato import MenuRegistrarContrato
from src.board_and_play_poo.app.menus.menu_contrato import MenuContrato

tb = Tabela()
db = Database("teste")
tb.create_table(db)

repo_jogo_aluguel = RepositoryJogoAluguel(db, tb)
repo_item_aluguel = RepositoryItemAluguel(db, tb)
repo_aluguel = RepositoryAluguel(db, tb)

service_aluguel = ServiceAluguel(
    repo_aluguel,
    repo_item_aluguel,
    repo_jogo_aluguel
)

menu_registrar = MenuRegistrarContrato(service_aluguel)

class App():
    """Aplicação, onde são guardados os menus que serão chamados para a interação do usuáiro"""
    def menu_principal():
        '''Menu principal''' 
        print("Inicializando o sistema...")
        while True: 
            while True:
                try:
                    print("\nBoard and play")
                    print("-" * 20)
                    print("1 - Registrar contrato\n2 - Gerar venda\n3 - Estoque\n4 - Contratos\n5 - Vendas\n6 - Colaboradores\n7 - Cliente\n8 - Sair")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    App.menu_registrar_contrato()
                case 2:
                    App.menu_gerar_venda()
                case 3:
                    App.menu_estoque()
                case 4:
                    MenuContrato().menu_contrato()
                case 5:
                    App.menu_venda()
                case 6:
                    App.menu_colaborador()
                case 7:
                    App.menu_cliente()
                case 8:
                    print("\nDesligando sistema...")
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_estoque():
        '''Menu das classes que herdam de Produto'''
        while True:
            while True:
                try:
                    print("\nEstoque")
                    print("-" * 20)
                    print("1 - Jogo aluguel\n2 - Jogo venda\n3 - Consumíveis\n4 - Acessórios\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuJogoAluguel().menu_jogo_aluguel()
                case 2:
                    MenuJogoVenda.menu_jogo_venda()
                case 3:
                    App.menu_consumivel()
                case 4:
                    App.menu_acessorio()
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_registrar_contrato():
        MenuRegistrarContrato.menu_registrar_contrato()