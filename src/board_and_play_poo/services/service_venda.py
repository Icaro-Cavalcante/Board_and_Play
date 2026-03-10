class ServiceVenda:
    """Classe que faz a comunicação entre a Aplicação e o Repository"""
    
    def __init__(self, repo_venda, repo_item_venda, repo_produto):
        self.repo_venda = repo_venda
        self.repo_item_venda = repo_item_venda
        self.repo_produto = repo_produto

    def adicionar_item(self, carrinho, produto_id, quantidade, valor_unitario):
        """Cria um carrinho onde se adicionam os itens pertencentes a uma Venda"""
        item = {
            "produto_id": produto_id,
            "quantidade": quantidade,
            "valor_unitario": valor_unitario
        }
        carrinho.append(item)
        return "Item adicionado"

    def gerar_venda(self, venda, carrinho):
        """Cria uma instância de Aluguel que representa um contrato de aluguel"""
        if not carrinho:
            return "Carrinho vazio"
        venda_id = self.repo_venda.create(venda)
        for item in carrinho:
            dados = (
                venda_id,
                item["produto_id"],
                item["quantidade"],
                item["valor_unitario"]
            )
            self.repo_item_venda.create(dados)
            self.repo_produto.baixar_estoque(
                item["produto_id"],
                item["quantidade"]
            )
        return f"Venda {venda_id} criada"