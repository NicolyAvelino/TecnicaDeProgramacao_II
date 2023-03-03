from abc import ABC, abstractmethod

# Classe abstrata que define um método abstrato a ser implementado por suas subclasses
class Transporte(ABC):
    @abstractmethod
    def entregar(self, pacote):
        pass

# Subclasse de Transporte
class Caminhao(Transporte):
    def entregar(self, pacote):
        return f"Caminhão está entregando o pacote {pacote}"

# Subclasse de Transporte
class Navio(Transporte):
    def entregar(self, pacote):
        return f"Navio está entregando o pacote {pacote}"

# Classe Factory Method
class FabricaTransporte:
    def criar_transporte(self, tipo_transporte):
        if tipo_transporte == "Caminhao":
            return Caminhao()
        elif tipo_transporte == "Navio":
            return Navio()
        else:
            raise ValueError("Tipo de Transporte inválido!")

# codigo cliente 
fabrica_transporte = FabricaTransporte()
caminhao = fabrica_transporte.criar_transporte("Caminhao")
navio = fabrica_transporte.criar_transporte("Navio")

# chamando o metodo
print(caminhao.entregar("ABC123"))
print(navio.entregar("XYZ789"))