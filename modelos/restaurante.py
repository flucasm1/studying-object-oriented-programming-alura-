class Restaurante:
    restaurantes = []
    def __init__(self, nome, cat):
        self._nome = nome.upper()
        self._cat = cat.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cat}'
    
    def listar_r():
        print(f'{'Nome do Restaurante:'.ljust(25)} | {'Classe do Restaurante:'.ljust(25)} | {'Status:'.ljust(25)}')
        for n in Restaurante.restaurantes:
            print(f'{n._nome.ljust(25)} | {n._cat.ljust(25)} | {n._ativo}') 
    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'

r_fantastico = Restaurante('Fantástico', 'Mexicana')
r_canada = Restaurante('Canadá Food', 'Canadense')

Restaurante.listar_r()