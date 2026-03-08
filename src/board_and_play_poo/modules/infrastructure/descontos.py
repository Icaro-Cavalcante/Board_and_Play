from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    """Entrega um método abstrato para definição em outras classes"""
    @abstractmethod
    def AplicarDesconto(self, preco: float):
        pass

class DescontoPorcent(EstrategiaDesconto):
    """Classe para realizar descontos em porcentagem"""
    def __init__(self, porcentagem):
        self.porcentagem = porcentagem

    def AplicarDesconto(self, preco):
        return preco * (1 - self.porcentagem / 100)
    
class DescontoValorFixo(EstrategiaDesconto):
    """Classe para aplicar descontos em valores decimais"""
    def __init__(self, valor):
        self.valor = valor

    def AplicarDesconto(self, preco):
        if preco < self.valor:
            while True:
                try:
                    resultado = float(input("Valor de desconto maior que preço do produto, digite novo valor: "))
                    break
                except ValueError:
                    print("Dado digitado incompatível.")
        return preco - self.valor