#Cristian Aguirre
#16/04

respuesta = 0

def sumar (x,y):
    respuesta = x + y
    return respuesta

sumar(5, 7)

print(respuesta)

resultado = 0

def sumar (x,y):
    global resultado #indica que queremos modificar la variable global
    resultado = x + y

sumar(5, 7)
print(resultado)