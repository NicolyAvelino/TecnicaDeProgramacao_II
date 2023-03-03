from abc import ABC, abstractmethod

# Classe abstrata que define um método abstrato a ser implementado por suas subclasses
class Portaria(ABC):
    @abstractmethod
    def liberarAcesso(self, entrada):
        pass

class Aluno(Portaria):
    def liberarAcesso(self, entrada):
        return f"tem relação com a instituição como {entrada}" 

class Funcionario(Portaria):
    def liberarAcesso(self, entrada):
        return f"tem relação com a instituição como {entrada}" 

class Professor(Portaria):
    def liberarAcesso(self, entrada):
        return f"tem relação com a instituição como {entrada}" 

class PublicoGeral(Portaria):
    def liberarAcesso(self, entrada):
        return f"tem relação com a instituição como {entrada}" 

class Acesso:
    def permitir_acesso(self, tipo_acesso):
        if tipo_acesso == "Aluno":
            return Aluno()
        elif tipo_acesso == "Funcionario":
            return Funcionario()
        elif tipo_acesso == "Professor":
            return Professor()
        elif tipo_acesso == "PublicoGeral":
            return PublicoGeral()
        else:
            return f"não tem nenhuma relação com a instituição, acompanhar até a secretária."

acesso = Acesso()
aluno = acesso.permitir_acesso("Aluno")
funcionario = acesso.permitir_acesso("Funcionario")
professor = acesso.permitir_acesso("Professor")
publicoGeral = acesso.permitir_acesso("PublicoGeral")

print(aluno.liberarAcesso("liberado"))
print(aluno.liberarAcesso("liberado"))
print(professor.liberarAcesso("liberado"))
print(publicoGeral.liberarAcesso("liberado"))