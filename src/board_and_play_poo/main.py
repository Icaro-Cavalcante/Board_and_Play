from modules.domain.alugaveis import Jogo_aluguel
from modules.domain.compraveis import Jogo_venda
from modules.services.venda import Venda
from modules.services.aluguel import Aluguel

def main():
    '''Função principal do sistema, a qual exibe a interface e permite a interação do usuário com as outras funcionalidades'''
    while True:
        print("Board and play")
        print("-" * 20)
        print("1 - Jogo aluguel\n2 - Jogo venda\n3 - Aluguel\n4 - Venda\n5 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            menu_jogo_aluguel()
        elif escolha == 2:
            menu_jogo_compra()
        elif escolha == 3:
            menu_aluguel()
        elif escolha == 4:
            menu_venda()
        elif escolha == 5:
            break
        else:
            print("Escolha inválida.\n")

def menu_jogo_aluguel():
    dic_atr = {1: "id", 2: "idade_min", 3: "num_jogadores", 4: "nome", 5: "data_aquisicao", 6: "descricao", 7: "tipo", 8: "status", 9: "custo_aquisicao", 10: "valor_sessao", 11: "valor_diaria"}
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
    dic_atr = {1: "id", 2: "idade_min", 3: "num_jogadores", 4: "nome", 5: "data_aquisicao", 6: "descricao", 7: "tipo", 8: "status", 9: "custo_aquisicao", 10: "valor_compra"}
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
                    elif atr in (9, 10):
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


def menu_aluguel():
    while True:
        print("\nMenu dos aluguéis")
        print("-" * 20)
        print("1 - Cadastrar aluguel\n2 - Consultar aluguel\n3 - Editar aluguel\n4 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            Aluguel.create()
        elif escolha == 2:
            id = int(input("Informe o ID: "))
            consultar_aluguel = Aluguel.read(id)
            if consultar_aluguel == None:
                print("Esse aluguel não existe")
            else:
                print(consultar_aluguel)
        elif escolha == 3:
            menu_edicao_aluguel()
        elif escolha == 4:
            break
        else:
            print("Atributo inválido")
                
def menu_edicao_aluguel():
    id = int(input("Escolha o ID do aluguel que deseja editar: "))
    consultar_aluguel = Aluguel.read(id)
    if consultar_aluguel == None:
        print("Esse aluguel não existe.")
    else:
        dicionario_atributo = {1: "id_produto", 2: "data_inicio", 3: "data_prevista_devolucao", 4: "multa_diaria", 5: "multa_avaria"}
        print("Atributos")
        print("-" * 20)
        for key in dicionario_atributo:
            print(f"{key} - {dicionario_atributo[key]}")
        escolha = int(input("Selecione um atributo: "))
        if escolha == 1:
            atributo_novo = int(input("Digite o atributo atualizado: "))
            nome_atributo = dicionario_atributo[escolha]
            Aluguel.update(id, nome_atributo, atributo_novo)
        elif escolha in (2, 3):
            atributo_novo = str(input("Digite o atributo atualizado: "))
            nome_atributo = dicionario_atributo[escolha]
            Aluguel.update(id, nome_atributo, atributo_novo)
        elif escolha in (4, 5):
            atributo_novo = float(input("Digite o atributo atualizado: "))
            nome_atributo = dicionario_atributo[escolha]
            Aluguel.update(id, nome_atributo, atributo_novo)
        else:
            print("Atributo inválido")
        

        
        

def menu_venda():
    while True:
        print("\nMenu de vendas")
        print("-" * 20)
        print("1 - Cadastrar venda\n2 - Consultar venda\n3 - Editar venda\n4 - Sair")
        escolha = int(input("Selecione uma opção: "))
        if escolha == 1:
            Venda.create()
        elif escolha == 2:
            print(Venda.read(int(input("Digite o id da venda para busca: "))))
        elif escolha == 3:
            id = int(input("Escolha o ID da venda que deseja editar: "))
            consultar_venda = Venda.read(id)
            if consultar_venda == None:
                print("Essa venda não existe")
            else:
                dic_venda = {1: "id_produto", 2: "tipo_produto"}
                print("Atributos")
                print("-" * 20)
                print("1 - id_produto\n2 - tipo_produto")
                try:
                    escolha = int(input("Selecione um atributo: "))
                    if escolha == 1:
                        atr = int(input("Digite o valor para substituição: "))
                        Venda.update(id, dic_venda[escolha], atr)
                    elif escolha == 2:
                        atr = str(input("Digite o dado para substituição: "))
                        Venda.update(id, dic_venda[escolha], atr)
                    else: raise ValueError
                except ValueError:
                    print("Entrada inválida.")
        elif escolha == 4:
            break
        else: print("Entrada não reconhecida.")
            

if __name__ == "__main__":
    main()