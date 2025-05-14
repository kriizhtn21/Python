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

def fortuna():
    random_fortuna = random.randint(0, len(opciones) -1)
    


    if random_fortuna == 0:
        opcion = opciones[0]
    elif random_fortuna == 1:
        opcion = opciones[1]
    elif random_fortuna == 2:
        opcion = opciones[2]
    elif random_fortuna == 3:
        opcion = opciones[3]
    elif random_fortuna == 4:
        opcion = opciones[4]
    elif random_fortuna == 5:
        opcion = opciones[5]
    elif random_fortuna == 6:
        opcion = opciones[6]
    elif random_fortuna == 7:
        opcion = opciones[7]
    elif random_fortuna == 8:
        opcion = opciones[8]
    else:
        print("Error")

    print(opcion)

fortuna()
fortuna()
fortuna()
