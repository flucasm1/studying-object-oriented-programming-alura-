class Restaurante:
    restaurantes = []
    def __init__(self, nome, cat):
        self._nome = nome.upper()
        self._cat = cat.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._cat}'

    @classmethod
    def listar_r(cls):
        print(f'{'Nome do Restaurante:'.ljust(25)} | {'Classe do Restaurante:'.ljust(25)} | {'Status:'.ljust(25)}')
        for n in Restaurante.restaurantes:
            print(f'{n._nome.ljust(25)} | {n._cat.ljust(25)} | {n.ativo}') 
            

    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'

    def change_ativo(self):
        self._ativo = not self._ativo

r_fantastico = Restaurante('Fantástico', 'Mexicana')
r_fantastico.change_ativo()
r_canada = Restaurante('Canadá Food', 'Canadense')

#Restaurante.listar_r()
