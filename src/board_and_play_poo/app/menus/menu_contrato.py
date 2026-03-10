from src.board_and_play_poo.repositories.repository_aluguel import RepositoryAluguel
from src.board_and_play_poo.services.service_aluguel import ServiceAluguel
from src.board_and_play_poo.repositories.repository_item_aluguel import RepositoryItemAluguel
from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.modules.domain.alugueis import Aluguel
from src.board_and_play_poo.database.database import Database
from src.board_and_play_poo.database.tabelas import Tabela

tb = Tabela()
db = Database("real")
tb.create_table(db) # Criando tabelas do db de test

aluguel_repo = RepositoryAluguel(db, tb)
item_repo = RepositoryItemAluguel(db, tb)
jogo_repo = RepositoryJogoAluguel(db, tb)
service = ServiceAluguel(aluguel_repo, item_repo, jogo_repo)

class MenuContrato:    
    def menu_contrato(self):
        '''Menu das consultas dos contratos de aluguel do sistema'''
        while True:
            while True:
                try:
                    print("\nContratos")
                    print("-" * 20)
                    print("1 - Consultar por ID\n2 - Consultar contratos abertos\n3 - Consultar contratos alterados\n4 - Consultar contratos fechados\n5 - Fechar contrato\n6 - Voltar")
                    escolha = int(input("Selecione uma opção: "))
                    break
                except ValueError:
                    print("\nA opção deve ser um número inteiro.\n")
            match escolha:
                case 1:
                    MenuContrato.menu_consultar_id()
                case 2:
                    MenuContrato.menu_consultar_status("ABERTO")
                case 3:
                    MenuContrato.menu_consultar_status("ALTERADO")
                case 4:
                    MenuContrato.menu_consultar_status("FECHADO")
                case 5:
                    MenuContrato.menu_fechar_contratO()
                case 6:
                    break
                case _:
                    print("Escolha inválida.\n")

    def menu_consultar_id():
        '''Menu para interagir com a função de consultar por id'''
        while True:
            try:
                id = int(input("Insira o id que deseja buscar: "))
                break
            except ValueError:
                print("\nId precisa ser um número inteiro!\n")
        contrato_consulta = aluguel_repo.read(id)
        if contrato_consulta:
            while True:
                while True:
                    try:
                        print(f"\nContrato {contrato_consulta.aluguel_id}")
                        print("-" * 20)
                        print("1 - Consultar atributos\n2 - Consultar itens\n3 - Sair")
                        escolha = int(input("Selecione uma opção: "))
                        break
                    except ValueError:
                        print("\nA opção deve ser um número inteiro.\n")
                match escolha:
                    case 1:
                        print(contrato_consulta)
                    case 2:
                        tuplas = item_repo.buscar_por_aluguel(contrato_consulta.aluguel_id)
                        for tupla in tuplas:
                            print("")
                            item_repo.imprimir_dados(tupla)
                            print("")
                    case 3:
                        break
                    case _:
                        print("Escolha inválida.\n")
        else:
            print("Não foi possível conectar")
            
    def menu_consultar_status(status):
        '''Menu para interagir com os contratos do status recebido'''
        contrato_consulta = (aluguel_repo.read_especifico(status))
        if contrato_consulta:
            for contrato in contrato_consulta:
                print("")
                print(contrato)
                print("")
        else:
            print("Não foi possível achar contratos.")

    def menu_fechar_contratO():
        global service
        print("\n" + "="*30)
        print("FECHAMENTO DE CONTRATO")
        print("="*30)
        
        try:
            aluguel_id = int(input("Digite o ID do aluguel: "))
            contrato = aluguel_repo.read(aluguel_id)

            if not contrato or contrato.status == "FECHADO":
                print("\nContrato inexistente ou já encerrado")
                return

            # 1. Cálculo Automático
            valor_sistema = service.calcular_total_contrato(aluguel_id)
            print(f"\nValor calculado pelo sistema (diárias/sessões): R$ {valor_sistema}")
            
            # 2. Adição de Multas Manuais
            multas_extras = float(input("Valor de multas extras (avarias/perda, 0 para nenhuma): "))
            total_final = valor_sistema + multas_extras
            
            print(f"\nTOTAL A PAGAR: R$ {total_final:.2f}")
            print("-" * 20)

            forma_pag = input("Forma de pagamento (PIX/DEBITO/CREDITO/DINHEIRO): ").upper()
            
            confirmar = input(f"Confirmar recebimento e fechamento? (S/N): ").upper()
            
            if confirmar == "S":
                comprovante = Aluguel.gerar_comprovante()
                dados_financeiros = [comprovante, total_final, forma_pag, "ALUGUEL"]
                
                resultado = service.finalizar_aluguel(aluguel_id, dados_financeiros)
                print(f"\n[OK] {resultado}")
            else:
                print("\nInput inválido, cancelando operação")

        except ValueError:
            print("\n[Erro] Entrada inválida. Digite apenas números")

