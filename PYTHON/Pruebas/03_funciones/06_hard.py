#cristiannnnnnnnnnnn

def calcular_nota(puntaje):
    """calcular la nota en base al puntaje ingresado.
    El puntaje maximo es 30 y la nota maxima es 7"""

    if puntaje < 0 or puntaje > 30:
        return "Puntaje no valido"
    
    #formula para calcular la nota
    nota = 1+ (6* puntaje/30)

    #redondear la nota a 2 decimales
    return round(nota, 2)

#solicitar el puntaje al usuario

try:
    puntaje_usuario = float(input("Introduce el puntaje (0-30): "))
    nota_final = calcular_nota(puntaje_usuario)
    print(f"Tu nota es: {nota_final}")
except ValueError:
    print("Error: Debes ingresar un numero valido")
    