from datetime import date, datetime

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