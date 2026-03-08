class MenuVenda:    
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