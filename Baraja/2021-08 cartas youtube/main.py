import juegoCasino

print('Juego de cartas hecho en Python')

juego = juegoCasino.Juego()

while not juego.terminado():
    juego.ronda()
