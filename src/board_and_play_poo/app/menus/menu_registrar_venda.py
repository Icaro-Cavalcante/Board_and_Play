from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.repositories.repository_item_venda import RepositoryItemVenda
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)

produto_repo = RepositoryProduto(db, tb)
jogo_repo = RepositoryJogo(db, tb)
jogo_a_repo = RepositoryJogoAluguel(db, tb)
item_v_repo = RepositoryItemVenda(db, tb)

class MenuRegistrarVenda:
    """Menu das classes Venda e ItemVenda"""  
    # comprovante, ForPagmt,  nota_fiscal, cliente_id, colaborador_id
    def menu_gerar_venda():
        print("\nRegistro de Venda\n\nCaso deseje sair anterior ao cadastro de fato, ao sistema pedir o id de cliente digite qualquer caractere não numérico")
        print("-" * 20)
        while True:
            lista_IV = []
            try:
                comp = str(input("\nDigite o comprovante de transação: "))
                form = str(input("\nDigite a forma de pagamento: "))
                nota = str(input("\nDigite a nota fiscal da venda: "))
                cli_id = int(input("\nDigite o id do cliente: "))
                col_id = int(input("\nDigite o id do colaborador realizando a venda: "))
                while True:
                    try:
                        print("\n", "-" * 20, "Iniciando cadastro de itens vendidos", "-" * 20, "\n")
                        produto_id = int(input("\nDigite o id do produto a ser vendido: "))
                        prod = produto_repo.read(produto_id)
                        if MenuRegistrarVenda.check_alugavel(prod): raise ValueError
                        qtd = int(input("Digite a quantidade de itens sendo vendidos: "))
                        if qtd < 1: raise ValueError
                        prc = float(input("Digite o preço de uma unidade desse produto: "))
                        if prc <= 0: raise ValueError
                        lista_guia = [produto_id, qtd, prc]
                        lista_IV.append(lista_guia)
                        continuar = int(input("Digite 1 caso ainda há jogos na venda não inclusos, do contrário, digite qualquer outra tecla: "))
                        if continuar != 1: break
                    except ValueError:
                        print("Dado inválido inserido, reiniciando cadastro")
                    item_v_repo.gerar_venda(lista_IV, comp, form, nota, cli_id, col_id)
                    print("Venda cadastrada")
            except ValueError:
                print("Dado inválido inserido, saindo do cadastro")

    def check_alugavel(prod):
        if prod:
            if prod.categoria == "JOGO":
                jog = jogo_repo.find(prod.id)
                jog_a = jogo_a_repo.find(jog.id)
                if jog_a:
                    return True
MenuRegistrarVenda.menu_gerar_venda()