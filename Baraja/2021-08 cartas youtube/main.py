import juegoCasino

print('Juego de cartas hecho en python')

juego = juegoCasino.Juego()

while not juego.terminado():
    juego.ronda()
