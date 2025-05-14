#crstianooooo


def suma(**kwargs):
    print(type(kwargs))

suma(x=3)

def suma(**kwargs): 
    s = 0
    for key, value in kwargs.items(): #cuanto tienes un diccionario, puedes usar el metodo items() para 
        print(key, "=", value)        #recorrer los elementos del diccionario, las claves y los valores
        s += value
    return s

resultado = suma(x=3, y=5, z=7)
#salida
#x = 3
#y = 5
#z = 7
#resultado = 15
