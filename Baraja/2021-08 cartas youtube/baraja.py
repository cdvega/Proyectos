import random


class Carta:
    def __init__(self, etiqueta, valor, palo):
        self.etiqueta = etiqueta
        self.valor = valor
        self.palo = palo

    def mostrar(self, numeracion=None):
        print((str(numeracion) + '. ' if numeracion !=
              None else '') + self.etiqueta)

    @staticmethod
    def cargarCartas():
        baraja = []
        etiquetas = ['As', 'Dos', 'Tres', 'Cuatro', 'Cinco',
                     'Seis', 'Siete', 'Sota', 'Caballo', 'Rey']
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        for p in palos:
            for i in range(10):
                baraja.append(Carta(f'{etiquetas[i]} de {p}', valores[i], p))
        return baraja


def mezclar(mazo):
    random.shuffle(mazo)
    return mazo
