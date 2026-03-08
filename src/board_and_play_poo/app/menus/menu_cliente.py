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