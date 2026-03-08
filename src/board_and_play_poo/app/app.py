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
                    App.menu_contrato()
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
                    App.menu_jogo_aluguel()
                case 2:
                    App.menu_jogo_venda()
                case 3:
                    App.menu_consumivel()
                case 4:
                    App.menu_acessorio()
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")