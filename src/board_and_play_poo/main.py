from modules.domain.alugaveis import Jogo_aluguel

def main():
    '''Função principal do sistema, a qual exibe a interface e permite a interação do usuário com as outras funcionalidades'''
    while True:
        print("Board and play")
        print("-" * 20)
        print("1 - Jogo aluguel\n2 - Jogo venda\n3 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            menu_jogo_aluguel()
        elif escolha == 2:
            print("Funcionalidade em desenvolvimento.\n")
        elif escolha == 3:
            break
        else:
            print("Escolha inválida.\n")

def menu_jogo_aluguel():
    while True:
        print("\nMenu dos jogos alugáveis")
        print("-" * 20)
        print("1 - Cadastrar jogo alugável\n2 - Consultar jogo alugável\n3 - Editar jogo alugável\n4 - Deletar jogo alugável\n5 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            Jogo_aluguel.create()
        elif escolha == 2:
            print("Funcionalidade em desenvolvimento.\n")
        elif escolha == 3:
            print("Funcionalidade em desenvolvimento.\n")
        elif escolha == 4:
            print("Funcionalidade em desenvolvimento.\n")
        elif escolha == 5:
            break
        else:
            print("Escolha inválida.\n")

if __name__ == "__main__":
    main()