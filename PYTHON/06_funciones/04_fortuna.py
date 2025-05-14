#Cristian Aguirre
#14/04

import random

opciones = [
    "no persigas la felicidad, creala",
    "todas las cosas son dificiles antes de ser faciles",
    "el pajaro madrugador consigue el gusano, pero el segundo raton se llama queso",
    "alguien en tu vida necesita una carta de tu parte",
    "no solo pienses. actua",
    "la fortuna que buscas esta en otra galleta",
    "!ayuda! ¡estoy prisionero en una panaderia china!"
]

def galleta_de_la_fortuna():
    fortuna_aleatoria = random.randint(0, len(opciones) - 1)
    print(opciones[fortuna_aleatoria])

galleta_de_la_fortuna()
galleta_de_la_fortuna()
galleta_de_la_fortuna()