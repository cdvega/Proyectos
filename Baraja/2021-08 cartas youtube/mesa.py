from baraja import *


class Mesa:
    def __init__(self):
        self.mazo = Carta.cargarCartas()
        self.cartasSobre = []

    def mezclar(self):
        self.mazo = mezclar(self.mazo)

    def mostrar(self):
        return self.mazo[0].etiqueta

    def mostrarMesa(self, seleccion=False):
        for i, carta in enumerate(self.cartasSobre):
            carta.mostrar(i+1 if seleccion else None)

    def ponerCarta(self, carta):
        self.cartasSobre.append(carta)
