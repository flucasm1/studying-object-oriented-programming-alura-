from abc import ABC, abstractmethod
class Veiculo:
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor

    def __str__(self):
        return f'Carro {self._nome}, cor {self._cor}'

    @abstractmethod
    def ligar(self):
        pass

class Carro(Veiculo): 
    def ligar(self):
        print(f"O {self._nome} ligou!")