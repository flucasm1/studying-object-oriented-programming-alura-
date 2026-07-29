from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
restaurante_sabor = Restaurante('Saboroso', 'Variado')
suco_melancia = Bebida('Suco de melancia', 5.00, 'grande', 'Refrescante')

def main():
    print(suco_melancia)

if __name__ == '__main__':
    main()


    