#cristiannoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


#pedir Numero
def pedir_numero():
    try:
        numero = int(input('escribe un numero entero:'))
    except ValueError:
        print('no es un numero entero')

pedir_numero()



#Division segura
def division_segura():
    try:
        numerador = int(input('escribe el numerador: '))
        denominador = int(input('escribe el denominador: '))
        resultado = numerador / denominador
    except ZeroDivisionError:
        print('no se puede dividir entre cero')
    except ValueError:
        print('no es un numero entero')

division_segura()




#mostrar_elemento

def mostrar_elemento():
    frutas = ['manzana', 'banana', 'naranja']
    try:
        indice = int(input('Elige una posicion (0 a 2) '))
        print("Fruta elegida:",frutas[indice])
    except IndexError:
        print('indice no existente')
    except ValueError:
        print('no es un numero entero')

mostrar_elemento()




#buscar_cantante
def buscar_cantante():
    cantante = {
        'nombre': 'Freddie Mercury',
        'pais': 'Reino Unido',
    }
    try:
        clave = input('que quieres saber? (nombre o pais) ')
        print ("resultado:", cantante[clave])
    except KeyError:
        print('no existe esa clave')

buscar_cantante()



#pedir_numero_repetido
def pedir_numero_repetido():
    while True:
        try:
            numero = int(input('escribe un numero entero:'))
            print("Gracias, tu numero es:", numero)
            break
        except ValueError:
            print('no es un numero valido, intenta de nuevo')

pedir_numero_repetido()