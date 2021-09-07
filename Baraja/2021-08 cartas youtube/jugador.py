class Jugador:
    def __init__(self, nombre, esBot):
        self.nombre = nombre
        self.esBot = esBot
        self.mano = []  # cartas en la mano del jugador

    def ponerMano(self, mano):
        self.mano = mano

    def cogerCarta(self, carta):
        '''Añade carta a la mano del jugador'''
        self.mano.append(carta)

    def mostrarMano(self, seleccion=False):
        '''Muestra las cartas del jugador'''
        for i, carta in enumerate(self.mano):
            carta.mostrar((i+1) if seleccion else None)

    def poseeValorCarta(self, valor):
        for carta in self.mano:
            if carta.valor == valor:
                return True
        return False
