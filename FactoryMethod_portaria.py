from abc import ABC, abstractmethod

# Classe abstrata que define um método abstrato a ser implementado por suas subclasses
class Portaria(ABC):
    @abstractmethod
    def liberarAcesso(self, entrada):
        pass

nome = input("Qual o seu nome?")
tipo_acesso = input("Qual a sua relação com a Fatec: (Digite somente o número) \n1- Aluno \n2- Professor \n3- Funcionário \n4- Público Geral \n")

# Subclasse de Portaria
class Aluno(Portaria):
    def liberarAcesso(self, entrada):
        return f"{nome} tem relação com a instituição como Aluno {entrada}"

# Subclasse de Portaria
class Professor(Portaria):
    def liberarAcesso(self, entrada):
        return f"{nome} tem relação com a instituição como Professor {entrada}"

# Subclasse de Portaria
class Funcionario(Portaria):
    def liberarAcesso(self, entrada):
        return f"{nome} tem relação com a instituição como Funcionário {entrada}"
    
# Subclasse de Portaria
class PublicoGeral(Portaria):
    def liberarAcesso(self, entrada):
        return f"{nome} tem relação com a instituição como Público Geral {entrada}"

# Classe Factory Method
class Acesso:
    def permitir_acesso(self, tipo_acesso):
        if tipo_acesso == 1:
            return Aluno()
        elif tipo_acesso == 2:
            return Professor()
        elif tipo_acesso == 3:
            return Funcionario()
        elif tipo_acesso == 4:
            return PublicoGeral()
        else:
            return f"{nome} não tem nenhuma relação com a instituição, acompanhar até a secretária."

# codigo cliente 
# Acesso()
acesso = Acesso()
aluno = acesso.permitir_acesso("Aluno")
professor = acesso.permitir_acesso("Professor")
funcionario = acesso.permitir_acesso("Funcionario")
publicoGeral = acesso.permitir_acesso("Publico Geral")

print(aluno.liberarAcesso())
# Aluno = Acesso.permitir_acesso(1)
# Professor = Acesso.permitir_acesso(2)
# Funcionario = Acesso.permitir_acesso(3)
# PublicoGeral = Acesso.permitir_acesso(4)


# # chamando o metodo
# print(Aluno.permitir_acesso())