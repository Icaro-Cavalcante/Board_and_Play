class MenuContrato:    
    def menu_contrato():
        '''Menu das consultas dos contratos de aluguel do sistema'''
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