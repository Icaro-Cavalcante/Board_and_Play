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
        match escolha:
            case 1:
                menu_jogo_aluguel()
            case 2:
                menu_jogo_compra()
            case 3:
                menu_aluguel()
            case 4:
                menu_venda()
            case 5:
                break
            case _:
                print("Escolha inválida.\n")

def menu_jogo_aluguel():
    while True:
        print("\nMenu dos jogos alugáveis")
        print("-" * 20)
        print("1 - Cadastrar jogo alugável\n2 - Consultar jogo alugável\n3 - Editar jogo alugável\n4 - Deletar jogo alugável\n5 - Sair")
        escolha = int(input("Selecione uma opção: "))
        match escolha:
            case 1:
                Jogo_aluguel.create()
            case 2:
                while True:
                    try:
                        id = int(input("Digite o ID do jogo que deseja consultar: "))
                        break
                    except ValueError:
                        print("\nO ID precisa ser um número inteiro.\n")
                tupla = Jogo_aluguel.read(id)
                if tupla == None:
                    print("Esse jogo não foi encontrado.")
                else:
                    objeto = Jogo_aluguel.tupla_objeto(tupla)
                    print(objeto)
            case 3:
                menu_edicao_jogo_aluguel()
            case 4:
                id = int(input("Digite o id do jogo que será deletado: "))
                Jogo_aluguel.delete(id)
            case 5:
                break
            case _:
                print("Escolha inválida.\n")

def menu_edicao_jogo_aluguel():
    dic_atr = {1: "id_produto", 2: "idade_min", 3: "num_jogadores", 4: "nome", 5: "data_aquisicao", 6: "descricao", 7: "tipo", 8: "status", 9: "custo_aquisicao", 10: "valor_sessao", 11: "valor_diaria"}
    while True:
        try:
            id = int(input("Digite o id do jogo que será editado: "))
            break
        except ValueError:
            print("\nInsira um ID válido. É necessário que seja um número inteiro.\n")
    id_read = Jogo_aluguel.read(id) 
    if id_read == None:
        print("\nJogo não encontrado.")
    else:
        print("\nJogo encontrado\n")
        while True:
            try:
                print("===Atributos===")
                for atributo in dic_atr:
                    print(f"{atributo} - {dic_atr[atributo]}")
                atr = int(input("Digite qual atributo será editado: "))
                match atr:
                    case 1 | 2 | 3:
                        upd = int(input("Digite o número para substituição: "))
                    case 4 | 5 | 6 | 7:
                        upd = str(input("Digite o dado para substituição: "))
                    case 8 | 9 | 10 | 11:
                        upd = int(input("Digite o número para substituição: "))
                    case _:
                        raise ValueError
                break
            except ValueError:
                print("\nInput digitado não válido.\n")
        atr = dic_atr[atr]
        Jogo_aluguel.update(id, atr, upd)
        print("Atributo atualizado.")

def menu_jogo_compra():
    while True:
        print("\nMenu dos jogos compráveis")
        print("-" * 20)
        print("1 - Cadastrar jogo comprável\n2 - Consultar jogo comprável\n3 - Editar jogo comprável\n4 - Deletar jogo comprável\n5 - Sair")
        escolha = int(input("Selecione uma opção: "))
        match escolha:
            case 1:
                Jogo_venda.create()
            case 2:
                print(Jogo_venda.read(int(input("Digite o id do jogo para busca: "))))
            case 3:
                menu_edicao_jogo_compra()
            case 4:
                id = int(input("Digite o id do jogo que será deletado: "))
                Jogo_venda.delete(id)
            case 5:
                break
            case _:
                print("Escolha inválida.\n")

def menu_edicao_jogo_compra():
    dic_atr = {1: "id_produto", 2: "idade_min", 3: "num_jogadores", 4: "nome", 5: "data_aquisicao", 6: "descricao", 7: "tipo", 8: "status", 9: "custo_aquisicao", 10: "valor_compra"}
    while True:
        try:
            id = int(input("Digite o id do jogo que será editado: "))
            break
        except ValueError:
            print("\nInsira um ID válido. É necessário que seja um número inteiro.\n")
    id_read = Jogo_venda.read(id)
    if id_read == None:
        print("\nJogo não encontrado.")
    else:
        while True:
            try:
                print("===Atributos===")
                for atributo in dic_atr:
                    print(f"{atributo} - {dic_atr[atributo]}")
                atr = int(input("Digite qual atributo será editado: "))
                match atr:
                    case 1 | 2 |3 |4:
                        upd = int(input("Digite o número para substituição: "))
                    case 4 | 5 | 6 | 7 | 8:
                        upd = str(input("Digite o dado para substituição: "))
                    case 9 | 10:
                        upd = int(input("Digite o número para substituição: "))
                    case _:
                        raise ValueError
                break
            except ValueError:
                print("\nInput digitado não válido.\n")
        atr = dic_atr[atr]
        Jogo_venda.update(id, atr, upd)

def menu_aluguel():
    while True:
        print("\nMenu dos aluguéis")
        print("-" * 20)
        print("1 - Cadastrar aluguel\n2 - Consultar aluguel\n3 - Editar aluguel\n4 - Sair")
        escolha = int(input("Selecione uma opção: "))
        match escolha:
            case 1:
                Aluguel.create()
            case 2:
                while True:
                    try:
                        id = int(input("Digite o ID do aluguel que deseja consultar: "))
                        break
                    except ValueError:
                        print("\nO ID precisa ser um número inteiro.\n")
                tupla = Aluguel.read(id)
                if tupla == None:
                    print("Esse aluguel não foi encontrado.")
                else:
                    objeto = Aluguel.tupla_objeto(tupla)
                    print(objeto)
            case 3:
                menu_edicao_aluguel()
            case 4:
                break
            case _:
                print("Atributo inválido.")
                
def menu_edicao_aluguel():
    while True:
        try:
            id = int(input("Escolha o ID do aluguel que deseja editar: "))
            break
        except ValueError:
            print("\nInsira um ID válido. É necessário que seja um número inteiro.\n")
    consultar_aluguel = Aluguel.read(id)
    if consultar_aluguel == None:
        print("Esse aluguel não existe.")
    else:
        while True:
            try:
                dicionario_atributo = {1: "id_produto", 2: "data_inicio", 3: "data_prevista_devolucao", 4: "multa_diaria", 5: "multa_avaria"}
                print("===Atributos===")
                for key in dicionario_atributo:
                    print(f"{key} - {dicionario_atributo[key]}")
                escolha = int(input("Selecione um atributo: "))
                match escolha:
                    case 1:
                        atributo_novo = int(input("Digite o atributo atualizado: "))
                    case 2 | 3:
                        atributo_novo = str(input("Digite o atributo atualizado: "))
                    case 4 | 5:
                        atributo_novo = float(input("Digite o atributo atualizado: "))
                    case _:
                        raise ValueError
                break
            except ValueError:
                print("\nInput digitado não válido.\n")
        atributo = dicionario_atributo[escolha]
        Jogo_venda.update(id, atributo, atributo_novo)

def menu_venda():
    while True:
        print("\nMenu de vendas")
        print("-" * 20)
        print("1 - Cadastrar venda\n2 - Consultar venda\n3 - Editar venda\n4 - Sair")
        escolha = int(input("Selecione uma opção: "))
        match escolha:
            case 1:
                Venda.create()
            case 2:
                while True:
                    try:
                        id = int(input("Digite o ID da venda que deseja consultar: "))
                        break
                    except ValueError:
                        print("\nO ID precisa ser um número inteiro.\n")
                tupla = Venda.read(id)
                if tupla == None:
                    print("Essa venda não foi encontrada.")
                else:
                    objeto = Venda.tupla_objeto(tupla)
                    print(objeto)
            case 3:
                menu_edicao_venda()
            case 4:
                break
            case _:
                print("Escolha inválida.\n")

def menu_edicao_venda():
    dic_venda = {1: "id_produto", 2: "tipo_produto"}
    while True:
        try:
            id = int(input("Escolha o ID da venda que deseja editar: "))
            break
        except ValueError:
            print("\nInsira um ID válido. É necessário que seja um número inteiro.\n")
    consultar_venda = Venda.read(id)
    if consultar_venda == None:
        print("Essa venda não existe")
    else:
        while True:
            try:
                print("===Atributos===")
                for atributo in dic_venda:
                    print(f"{atributo} - {dic_venda[atributo]}")
                escolha = int(input("Selecione um atributo: "))
                match escolha:
                    case 1:
                        atributo_novo = int(input("Digite o valor para substituição: "))
                    case 2:
                        atributo_novo = str(input("Digite o dado para substituição: "))
                    case _: raise ValueError
                break
            except ValueError:
                print("Entrada inválida.")
        atributo = dic_venda[escolha]
        Jogo_venda.update(id, atributo, atributo_novo)         

if __name__ == "__main__":
    main()