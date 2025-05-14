#cristianoooooo

def suma(a,b,c):
    return a + b + c

suma(5, 7, 9)

print(suma(5, 7, 9))

#El Problema es si quiero agragar otro numero
#solucion

def suma(*args):
    s = 0 #inicaliza la suma en 0
    for arg in args: #itera sobre los argumentos
        s += arg #suma cada argumento
    return s #retorna la suma total

resultado = suma(5, 7, 9, 10, 12, 15)
print(resultado) #imprime el resultado
#El resultado es 58

suma(1,1)
#salida 2



def suma (*args):
    return sum(args) #retorna la suma de todos los argumentos
#sum(args) es una funcion que suma todos los elementos de args

suma(1,2,3,4,5)
#salida 15

print(suma(1,2,3,4,5)) #imprime la suma de los argumentos
#salida 15
