from src.board_and_play_poo.modules.domain.alugueis import Aluguel
from src.board_and_play_poo.services.service_aluguel import ServiceAluguel
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.repositories.repository_aluguel import RepositoryAluguel
from src.board_and_play_poo.modules.domain.jogo_aluguel import JogoAluguel
from src.board_and_play_poo.repositories.repository_item_aluguel import RepositoryItemAluguel
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela
from src.board_and_play_poo.repositories.repository_cliente import RepositoryCliente
from src.board_and_play_poo.repositories.repository_colaborador import RepositoryColaborador
from datetime import datetime

tb = Tabela()
db = Database("real")
tb.create_table(db) # Criando tabelas do db de test

aluguel_repo = RepositoryAluguel(db, tb)
jogo_aluguel_repo = RepositoryJogoAluguel(db, tb)
item_repo = RepositoryItemAluguel(db, tb)
cliente_repo = RepositoryCliente(db, tb)
colaborador_repo = RepositoryColaborador(db, tb)
service = ServiceAluguel(aluguel_repo, item_repo, jogo_aluguel_repo)

class MenuRegistrarContrato:
    """Menu das classes Aluguel e ItemAluguel"""

    def __init__(self, service_aluguel):
        MenuRegistrarContrato.service = service_aluguel

    def menu_registrar_contrato():
        """Entrada padrão usada pelo App"""
        carrinho = []
        menu = MenuRegistrarContrato(service)

        while True:
        
            print("\nRegistrar contrato")
            print("----------------------")
            print("1 - Adicionar jogo")
            print("2 - Finalizar contrato")
            print("3 - Cancelar")
            opcao = input("Selecione: ")
            if opcao == "1":
                try:
                    jogo_id = int(input("ID do jogo: "))
                    jogo_aluguel = jogo_aluguel_repo.read(jogo_id)
                    if (jogo_aluguel):
                        valor_diaria = float(input("Valor diária: "))
                        valor_sessao = float(input("Valor sessão: "))
                        resposta = menu.service.adicionar_jogo_carrinho(
                            carrinho,
                            jogo_id,
                            valor_diaria,
                            valor_sessao
                        )
                        print(resposta)
                    else:
                        print("Esse jogo não existe")
                except ValueError:
                    print("Dado inválido inserido, retornando ao menu de registro")

            elif opcao == "2":
                aluguel = menu.criar_objeto_aluguel()
                if aluguel:
                    resposta = menu.service.gerar_contrato(
                        aluguel,
                        carrinho
                    )
                    print(resposta)
                    break
            elif opcao == "3":
                print("Operação cancelada")
                break

    def criar_objeto_aluguel(self):
        try:
            cliente_id = int(input("ID do cliente: "))
            cliente = cliente_repo.read(cliente_id)
            if cliente:
                colaborador_id = int(input("ID do colaborador: "))
                colaborador = colaborador_repo.read(colaborador_id)
                if colaborador:        
                    numero_contrato = input("Número do contrato: ")
                    
                    while True:
                        data_inicio = input("Data início (AAAA-MM-DD): ")
                        data_prevista = input("Data prevista devolução (AAAA-MM-DD): ")
                        
                        try:
                            d_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
                            d_prevista = datetime.strptime(data_prevista, '%Y-%m-%d')
                            
                            if d_prevista < d_inicio:
                                print("Erro: A data prevista não pode ser menor que a data de início.")
                            else:
                                break
                        except ValueError:
                            print("Erro: Formato de data inválido. Use AAAA-MM-DD.")
                else:
                    print("O colaborador não existe.")
                    return None
            else:
                print("O cliente não existe.")    
                return None
        except ValueError:
            print("Dado inválido inserido, retornando ao menu de registro")
            return None

# O id de transação será cadastrado como None, pois os atributos de Transacao sóo são relevante para um contrato com status 'FECHADO'
        
        aluguel = Aluguel(numero_contrato, data_inicio, data_prevista, None, "ABERTO", cliente_id, colaborador_id, None, None)
        return aluguel