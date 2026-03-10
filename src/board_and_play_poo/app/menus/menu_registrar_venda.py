from src.board_and_play_poo.repositories.repository_produto import RepositoryProduto
from src.board_and_play_poo.repositories.repository_jogo import RepositoryJogo
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.repositories.repository_item_venda import RepositoryItemVenda
from src.board_and_play_poo.repositories.repository_cliente import RepositoryCliente
from src.board_and_play_poo.repositories.repository_colaborador import RepositoryColaborador
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db)

produto_repo = RepositoryProduto(db, tb)
jogo_repo = RepositoryJogo(db, tb)
jogo_a_repo = RepositoryJogoAluguel(db, tb)
item_v_repo = RepositoryItemVenda(db, tb)
cli_repo = RepositoryCliente(db, tb)
col_repo = RepositoryColaborador(db, tb)

class MenuRegistrarVenda:
    """Menu das classes Venda e ItemVenda"""  
    def menu_gerar_venda():
        Gerar_venda()

def criar_venda(func):
    def wrapper(*args, **kwargs):
        '''Menu que irá serir para o registro de vendas e seus dados'''
        print("\nRegistro de Venda\n\nCaso deseje sair anterior ao cadastro de fato, ao sistema pedir o id de cliente digite qualquer caractere não numérico")
        print("-" * 20)
        while True:
            try:
                comp = str(input("\nDigite o comprovante de transação: "))
                form = str(input("\nDigite a forma de pagamento: "))
                nota = str(input("\nDigite a nota fiscal da venda: "))
                cli_id = int(input("\nDigite o id do cliente: "))
                if cli_repo.read(cli_id):
                    pass
                else:
                    print("\nCliente inserido não existe, saindo do cadastro")
                    return
                col_id = int(input("\nDigite o id do colaborador realizando a venda: "))
                if col_repo.read(col_id):
                    pass
                else:
                    print("\nColaborador inserido não existe, saindo do cadstro")
                    return
                lista_IV = []
                lista_IV = func(lista_IV)
                if lista_IV:
                 item_v_repo.gerar_venda(lista_IV, comp, form, nota, cli_id, col_id)
                print("Venda cadastrada")
            except ValueError:
                print("Dado inválido inserido, saindo do cadastro")
                return
            break
    return wrapper

def check_alugavel(prod):
    '''Verifica se o jogo é alugável, retorna true se é'''
    if prod:
        if prod.categoria == "JOGO":
            jog = jogo_repo.find(prod.id)
            jog_a = jogo_a_repo.find(jog.id)
            if jog_a:
                return True
                
@criar_venda
def Gerar_venda(lista_IV):
    while True:
        try:
            print("\n", "-" * 20, "Iniciando cadastro de itens vendidos", "-" * 20, "\n")
            produto_id = int(input("\nDigite o id do produto a ser vendido: "))
            prod = produto_repo.read(produto_id)
            if check_alugavel(prod): raise MemoryError
            qtd = int(input("Digite a quantidade de itens sendo vendidos: "))
            if qtd < 1: raise ValueError
            prc = float(input("Digite o preço de uma unidade desse produto: "))
            if prc <= 0: raise ValueError
            lista_guia = [produto_id, qtd, prc]
            lista_IV.append(lista_guia)
            continuar = int(input("Digite 1 caso ainda há jogos na venda não inclusos, do contrário, digite qualquer outra tecla: "))
            if continuar != 1: break
        except ValueError:
            print("\nDado inválido inserido, reiniciando cadastro de produtos")
        except MemoryError:
            print("\nTentativa de inserção de jogo alugável no carrinho, reiniciando cadstro de produtos")
    return lista_IV
MenuRegistrarVenda.menu_gerar_venda()