from src.board_and_play_poo.modules.domain.alugueis import Aluguel

class MenuRegistrarContrato:
    """Menu das classes Aluguel e ItemAluguel"""

    def __init__(self, service_aluguel):
        MenuRegistrarContrato.service = service_aluguel

    def menu_registrar_contrato():
        """Entrada padrão usada pelo App"""
        carrinho = []

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
                    valor_diaria = float(input("Valor diária: "))
                    valor_sessao = float(input("Valor sessão: "))
                    resposta = MenuRegistrarContrato.service.adicionar_jogo_carrinho(
                        carrinho,
                        jogo_id,
                        valor_diaria,
                        valor_sessao
                    )
                    print(resposta)
                except ValueError:
                    print("Dado inválido inserido, retornando ao menu de registro")
            elif opcao == "2":
                aluguel = MenuRegistrarContrato.criar_objeto_aluguel()
                resposta = MenuRegistrarContrato.service.gerar_contrato(
                    aluguel,
                    carrinho
                )
                print(resposta)
                break
            elif opcao == "3":
                print("Operação cancelada")
                break

    def criar_objeto_aluguel():
        try:
            cliente_id = int(input("ID do cliente: "))
            colaborador_id = int(input("ID do colaborador: "))
            numero_contrato = input("Número do contrato: ")
            data_inicio = input("Data início: ")
            data_prevista = input("Data prevista devolução: ")
        except ValueError:
            print("Dado inválido inserido, retornando ao menu de registro")

# O id de transação será cadastrado como None, pois os atributos de Transacao sóo são relevante para um contrato com status 'FECHADO'
        
        aluguel = Aluguel(numero_contrato, data_inicio, data_prevista, None, "ABERTO", cliente_id, colaborador_id, None, None)
        return aluguel