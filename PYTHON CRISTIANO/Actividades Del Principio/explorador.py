#Cristian Aguirre
#24-03-25
#Me Gusta Jugar A La Pelota

#1.Accede al tercer elemento

mi_lista = ["Cristiano Ronaldo", "Neymar Jr", "Lionel Messi", "Alexis Sanchez"]

indice = mi_lista.index("Alexis Sanchez")

print(indice)

#2.Cambia el valor del ultimo elemento

mi_lista[-1]="Arturo Vidal"

print(mi_lista)

#3.Agrega un nuevo elemento a la lista

mi_lista.append("Lamine Yamal")

print(mi_lista)

#4.Inserta un elemento en la segunda posicion de la lista

mi_lista.insert(2,"Vinicius Jr")

print(mi_lista)

#5.Elimina un elemento de la lista usando su valor

eliminado = mi_lista.pop(2)

print(mi_lista)

#6.Encuentra la posicion de un elemento especifico

indice = mi_lista.index("Cristiano Ronaldo")

print(indice)

#7.Ordena la lista alfabeticamente

mi_lista.sort()

print(mi_lista)

#8.Invierte el orden de la lista

mi_lista.reverse()

print(mi_lista)