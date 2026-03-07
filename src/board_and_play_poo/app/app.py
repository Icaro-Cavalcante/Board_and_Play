class App():
    def menu_principal():
        '''Menu principal.''' 
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
        '''Menu das classes que herdam de produto'''
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

    def menu_jogo_aluguel():
        '''Menu da classe jogo aluguel'''
        while True:
            while True:
                try:
                    print("\nJogos alugáveis")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Inativar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_jogo_venda():
        '''Menu da classe jogo venda'''
        while True:
            while True:
                try:
                    print("\nJogos vendíveis")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Inativar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_acessorio():
        '''Menu da classe acessorio'''
        while True:
            while True:
                try:
                    print("\nAcessorio")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Inativar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_consumivel():
        '''Menu da classe consumivel'''
        while True:
            while True:
                try:
                    print("\nConsumíveis")
                    print("-" * 20)
                    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar dados\n4 - Inativar\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

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
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

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
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_contrato():
        '''Menu das consultas dos contratos de aluguel do sistema.'''
        while True:
            while True:
                try:
                    print("\nContratos")
                    print("-" * 20)
                    print("1 - Consultar por ID\n2 - Consultar contratos ativos\n3 - Consultar contratos alterados\n4 - Consultar contratos fechados\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                   print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_venda():
        '''Menu das consultas das vendas do sistema.'''
        while True:
            while True:
                try:
                    print("\nContratos")
                    print("-" * 20)
                    print("1 - Consultar por ID\n2 - Consultar por cliente\n3 - Consultar por periodo\n4 - Consultar por método de pagamento\n5 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    print("\n===Função em desenvolvimento===\n")
                case 2:
                    print("\n===Função em desenvolvimento===\n")
                case 3:
                    print("\n===Função em desenvolvimento===\n")
                case 4:
                    print("\n===Função em desenvolvimento===\n")
                case 5:
                    break
                case _:
                    print("Escolha inválida.\n")
    
    def menu_registrar_contrato():
        print("\n===Função em desenvolvimento===\n")

    def menu_gerar_venda():
        print("\n===Função em desenvolvimento===\n")