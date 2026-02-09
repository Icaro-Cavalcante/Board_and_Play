from modules.domain.alugaveis import Jogo_aluguel
from modules.domain.compraveis import Jogo_venda

dic_atr = {1: "id", 2: "nome", 3: "custo_aquisicao", 4: "data_aquisicao", 5: "descricao", 6: "idade_min", 7: "num_jogadores", 8: "tipo", 9: "status", 10: "valor_sessao", 11: "valor_diaria"}

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
            menu_jogo_compra()
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
            print(Jogo_aluguel.read(int(input("Digite o id do jogo para busca: "))))

        elif escolha == 3:
            id = int(input("Digite o id do jogo que será editado: "))
            while True:
                try:
                    atr = int(input("Digite qual atributo será editado:\nid: 1    idade_min: 2    num_jogadores: 3\nnome: 4     data_aquisição: 5    descrição: 6\ntipo: 7    status: 8    custo_aquisição: 9\nvalor_sessão: 10    valor_diária: 11\n"))
                    if atr > 0 and atr < 4:
                        upd = int(input("Digite o número para substituição: "))
                    elif atr >= 4 and atr <= 8:
                        upd = str(input("Digite o dado para substituição: "))
                    elif atr >= 9 and atr <= 11:
                        upd = int(input("Digite o número para substituição: "))
                    else: raise ValueError
                    break
                except ValueError:
                    print("Input digitado não válido.")
            atr = dic_atr[atr]
            Jogo_aluguel.update(id, atr, upd)

        elif escolha == 4:
            id = int(input("Digite o id do jogo que será deletado: "))
            Jogo_aluguel.delete(id)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida.\n")

def menu_jogo_compra():
    while True:
        print("\nMenu dos jogos compráveis")
        print("-" * 20)
        print("1 - Cadastrar jogo comprável\n2 - Consultar jogo comprável\n3 - Editar jogo comprável\n4 - Deletar jogo comprável\n5 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            Jogo_venda.create()

        elif escolha == 2:
            print(Jogo_venda.read(int(input("Digite o id do jogo para busca: "))))

        elif escolha == 3:
            id = int(input("Digite o id do jogo que será editado: "))
            while True:
                try:
                    atr = int(input("Digite qual atributo será editado:\nid: 1    idade_min: 2    num_jogadores: 3\nnome: 4     data_aquisição: 5    descrição: 6\ntipo: 7    status: 8    custo_aquisição: 9\nvalor_compra(preço): 10\n"))
                    if atr > 0 and atr < 4:
                        upd = int(input("Digite o número para substituição: "))
                    elif atr >= 4 and atr <= 8:
                        upd = str(input("Digite o dado para substituição: "))
                    elif atr >= 9 and atr <= 10:
                        upd = int(input("Digite o número para substituição: "))
                    else: raise ValueError
                    break
                except ValueError:
                    print("\nInput digitado não válido.\n")
            atr = dic_atr[atr]
            Jogo_venda.update(id, atr, upd)

        elif escolha == 4:
            id = int(input("Digite o id do jogo que será deletado: "))
            Jogo_venda.delete(id)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida.\n")

if __name__ == "__main__":
    main()