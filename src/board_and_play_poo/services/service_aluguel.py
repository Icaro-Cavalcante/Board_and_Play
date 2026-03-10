from datetime import date, datetime
from src.board_and_play_poo.modules.domain.alugueis import Aluguel

class ServiceAluguel:
    """Classe que faz a comunicação entre a Aplicação e o Repository"""

    def __init__(self, repo_aluguel, repo_item, repo_jogo):
        self.repo_aluguel = repo_aluguel
        self.repo_item = repo_item
        self.repo_jogo = repo_jogo

    def adicionar_jogo_carrinho(self, carrinho, jogo_id, valor_diaria, valor_sessao):
        """Cria um carrinho onde se adicionam os itens pertencentes a um contrato de aluguel"""
        item = {
            "jogo_id": jogo_id,
            "valor_diaria": valor_diaria,
            "valor_sessao": valor_sessao
        }
        carrinho.append(item)
        return "Jogo adicionado ao carrinho"

    def gerar_contrato(self, aluguel, carrinho):
        """Cria uma instância de Aluguel que representa um contrato de aluguel"""
        if not carrinho:
            return "Carrinho vazio"
        aluguel_id = self.repo_aluguel.create(aluguel)
        for item in carrinho:
            item_dados = (
                aluguel_id,
                item["jogo_id"],
                item["valor_diaria"],
                item["valor_sessao"]
            )
            self.repo_item.create(item_dados)
            self.repo_jogo.update(
                item["jogo_id"],
                "status",
                "ALUGADO"
            )
        return f"Contrato {aluguel_id} criado com sucesso"
    
    def calcular_total_contrato(self, aluguel_id):
        """Calcula o valor total baseado em diárias, sessões e dias decorridos"""
        contrato = self.repo_aluguel.read(aluguel_id)
        itens = self.repo_item.buscar_por_aluguel(aluguel_id)
        
        if not contrato or not itens:
            return 0.0

        # Calcular diferença de dias (Data Início até Hoje)
        data_inicio = datetime.strptime(contrato.data_inicio, '%Y-%m-%d').date() if isinstance(contrato.data_inicio, str) else contrato.data_inicio
        hoje = datetime.now().date()
        dias_alugados = (hoje - data_inicio).days
        
        # Garantir pelo menos 1 diária se for devolvido no mesmo dia
        if dias_alugados <= 0:
            dias_alugados = 1

        total = 0.0
        for item in itens:
            # item[2] = valor_diaria, item[3] = valor_sessao (conforme sua tabela itens_aluguel)
            v_diaria = float(item[2])
            v_sessao = float(item[3])
            total += (v_diaria * dias_alugados) + v_sessao

        return round(total, 2)
    
    def finalizar_aluguel(self, aluguel_id, dados_transacao):
        from src.board_and_play_poo.repositories.repository_transacao import RepositoryTransacao
        trans_repo = RepositoryTransacao(self.repo_aluguel.database, self.repo_aluguel.table)
        
        transacao_id = trans_repo.create(dados_transacao)
        
        if isinstance(transacao_id, int):
            from datetime import datetime
            hoje = datetime.now().date()
            
            self.repo_aluguel.update(aluguel_id, "status", "FECHADO")
            self.repo_aluguel.update(aluguel_id, "transacao_id", transacao_id)
            self.repo_aluguel.update(aluguel_id, "data_devolucao_real", hoje)

            itens = self.repo_item.buscar_por_aluguel(aluguel_id)
            for item in itens:
                jogo_id = item[1]
                self.repo_jogo.update(jogo_id, "status", "DISPONIVEL")
            
            return f"Contrato {aluguel_id} encerrado com sucesso. Transação: {transacao_id}"
        
        return "Erro: Não foi possível processar o pagamento no banco de dados"