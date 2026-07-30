from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
restaurante_sabor = Restaurante('Saboroso', 'Variado')
suco_melancia = Bebida('Suco de melancia', 5.00, 'grande', 'Refrescante')
suco_melancia.aplicar_desconto()
restaurante_sabor.adicionar_no_cardapio(suco_melancia)
def main():
    restaurante_sabor.mostrar_cardapio


if __name__ == '__main__':
    main()


    