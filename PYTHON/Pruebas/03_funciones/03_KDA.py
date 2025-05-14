#cristianoo

def kda (k,d,a):
    """
    Calcula el ratio KDA de un jugador."""

    if d == 0:
        return "La cantidad de muertes no puede ser cero"
    return (k+a) /d

#Ejemplo de uso
resultado = kda(10, 5, 20)
print("El KDA es:", resultado)