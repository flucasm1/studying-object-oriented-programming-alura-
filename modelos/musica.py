class Musica:
    musicos = []
    def __init__(self, nome, estilo):
        self.nome = nome
        self.estilo = estilo
        self.banda = False
        Musica.musicos.append(self)
    def __str__(self):
        return (f'{self.nome} | {self.estilo}')

    def listar_musicos():
        for m in Musica.musicos:
            print(m)


alê = Musica('Alexandro', 'Rock')
jess = Musica('Jessica', 'Pop')


Musica.listar_musicos()