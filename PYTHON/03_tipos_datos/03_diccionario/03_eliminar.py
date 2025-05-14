#Cristian Aguirre
#23/04/25

mi_diccionario = {
    "nombre": "Cristian",
    "apellido": "Aguirre",
    "edad": 17,}

mi_diccionario.pop("nombre") # Elimina el elemento con la clave "nombre"

del mi_diccionario["apellido"] # Elimina el elemento con la clave "apellido"

mi_diccionario.popitem("edad") # Elimina el elemento con la clave "edad"


print(mi_diccionario) # Imprime el diccionario después de eliminar el elemento
