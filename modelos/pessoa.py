class Pessoa:
    pessoas = []
    def __init__(self, nome='', idade = 0, meses = '', prof ='' ):
        self._nome = nome
        self._idade = idade
        self._meses = meses
        self._prof = prof
        Pessoa.pessoas.append(self)
    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._prof} '

    @classmethod
    def listar(cls):
        print(f'{'Nome'.ljust(20)} | {'Profissão'.ljust(20)} | {'Aniversário'.ljust(20)} | {'Idade'.ljust(20)}')
        for n in Pessoa.pessoas:
            print(f'{n._nome.ljust(20)} | {n._prof.ljust(20)} | {n.meses.ljust(20)} | {n._idade}')

    @property
    def meses(self):
        return 'Sim' if self._meses == '12' else 'Não'

  
            
         




ronaldo = Pessoa('Ronaldo', 27, '12',  'Jogador de Futebol')
tetris = Pessoa('Tetris', 19, '9', 'Gamer')
Pessoa.listar()