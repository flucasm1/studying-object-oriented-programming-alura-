from .avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    def __init__(self, nome, cat):
        self._nome = nome.upper()
        self._cat = cat.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._cat}'

    @classmethod
    def listar_r(cls):
        print(f'{'Nome do Restaurante:'.ljust(25)} | {'Classe do Restaurante:'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status:'.ljust(25)}')
        for n in Restaurante.restaurantes:
            print(f'{n._nome.ljust(25)} | {n._cat.ljust(25)} | {str(n.media_nota).ljust(25)} | {n.ativo}') 
            

    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'

    def change_ativo(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_nota(self):
        if not self._avaliacao:
            return 'Nenhuma avaliação'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qnt_notas = len(self._avaliacao)
        media = round(soma_notas/qnt_notas, 1)
        return media