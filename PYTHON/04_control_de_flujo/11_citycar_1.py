#Cristian Aguirre
#4/14/25
#enfasi

altura = int(input("¿Cuanto mides? "))
creditos = int(input("¿Cuantos creditos tienes? "))

if altura >=137 and creditos >=10:
    print('Disfruta el viaje!')

elif altura <137 and creditos >=10:
    print("No eres lo suficientemente alto para viajar")

elif altura >=137 and creditos <10:
    print("No tienes suficientes creditos para viajar")

else:
    print('No cumples los requisitos para viajar')
