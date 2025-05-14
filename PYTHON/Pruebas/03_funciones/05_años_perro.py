#cristiann

def años_perro(nombre,edad):
    """calcula la edad de un perro en años humanos"""
    #Convertir la edad a años humanos
    edad_humana = edad * 7

    #Devolver el mensaje
    return f"{nombre} tiene {edad_humana} años en años humanos"

#Ejemplo de uso
print(años_perro("Toby", 5))
print(años_perro("Luna", 3))
print(años_perro("Max", 2))