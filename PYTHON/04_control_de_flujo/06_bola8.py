#Cristiano

import random

pregunta = input('Pregunta: ')

numeor_aleatorio = random.randint(1, 9)

if numeor_aleatorio == 1:
    respuesta = 'si, definitivamente'
elif numeor_aleatorio == 2:
    respuesta = 'con toda certeza que si'
elif numeor_aleatorio == 3:
    respuesta = 'sin duda alguna'
elif numeor_aleatorio == 4:
    respuesta = 'respuesta confusa, vuelve a preguntar'
elif numeor_aleatorio == 5:
    respuesta = 'Preguntame mas tarde'
elif numeor_aleatorio == 6:
    respuesta = 'mejor no decirte ahora '
elif numeor_aleatorio == 7:
    respuesta = 'mis fuentes dicen que no'
elif numeor_aleatorio == 8:
    respuesta = 'la persepectiva no es buena'
elif numeor_aleatorio == 9:
    respuesta = 'definitivamente no'
else:
    respuesta = 'error'

    print('bola 8 dice: ' + respuesta)

