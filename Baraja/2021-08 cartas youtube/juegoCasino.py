from jugador import Jugador
from mesa import Mesa
from utilidades import Utilidades, Colores


class Juego:
    def __init__(self):
        self.mesa = Mesa()
        self.mesa.mezclar()
        self.jugadores = []
        self.iniciarJugadores()

        # Repartimos 4 cartas a cada jugador
        for _ in range(4):
            for jugador in self.jugadores:
                jugador.cogerCarta(self.mesa.mazo.pop(0))

        # Ponemos dos cartas sobre la mesa
        for _ in range(4):
            self.mesa.ponerCarta(self.mesa.mazo.pop(0))

        # Game tests
        # jugadores[0].mostrarMano()
        # print(len(self.mesa.mazo))  # cartas que quedan por repartir

    def iniciarJugadores(self):
        numJugadores = Utilidades.preguntarNumero(
            'Número de jugadores humanos (0 a 4): ', 0, 4)
        for i in range(numJugadores):
            nombre = input(f'Nombre del jugador {i+1}: ')
            self.jugadores.append(Jugador(nombre, False))
        for i in range(4-numJugadores):
            self.jugadores.append(Jugador(f'BOT_{i+1}', True))

    def terminado(self):
        return False

    def ronda(self):
        '''Ronda del juego'''
        print(Colores.REVERSE+'Cartas en la mesa:'+Colores.ENDC)
        self.mesa.mostrarMesa(seleccion=True)
        for jugador in self.jugadores:
            self.jugar(jugador)

    def jugar(self, jugador):
        print(f'Es el turno de {jugador.nombre}')
        print(Colores.REVERSE+'Tus cartas:'+Colores.ENDC)
        jugador.mostrarMano(seleccion=True)
        opcion = Utilidades.preguntarOpciones(
            '¿Qué quieres hacer (c:Coger de la mesa, t:Tirar)? ', ['c', 't'])
        if opcion == 'c':
            print('Cartas en la mesa:')
            self.mesa.mostrarMesa(seleccion=True)
            posCartaEscogida = Utilidades.preguntarNumero(
                '¿Qué carta eliges? ', 1, len(self.mesa.cartasSobre))
            cartaEscogida = self.mesa.cartasSobre[posCartaEscogida-1]
            if not self.cartaEscogidaValida(jugador, cartaEscogida):
                print(
                    f'No puedes coger esa carta. No tienes carta de valor {cartaEscogida.valor}')
            print(
                f'Has elegido el {self.mesa.cartasSobre[posCartaEscogida-1].etiqueta}')

    def cartaEscogidaValida(self, jugador, cartaEscogida):
        return jugador.poseeValorCarta(cartaEscogida.valor)
