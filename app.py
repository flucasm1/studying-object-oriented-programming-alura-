from modelos.restaurante import Restaurante

restaurante_sabor = Restaurante('Saboroso', 'Variado')
restaurante_y = Restaurante('Y', 'Comida')
restaurante_x = Restaurante('X', 'Food')

restaurante_y.change_ativo()

def main():
    Restaurante.listar_r()

if __name__ == '__main__':
    main()


    