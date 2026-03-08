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