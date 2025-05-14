#cristianooooooooooooo


def auto_servicio(opcion):
    if opcion == 1:
        return "Hamburguesa"
    elif opcion == 2:
        return "Papas fritas"
    elif opcion == 3:
        return "Refresco"
    elif opcion == 4:
        return "Helado"
    elif opcion == 5:
        return "Big Mac"
    else:
        return "Opcion no valida"
    
def bienvenida():
    print("Bienvenido al auto servicio")
    print("1. Hamburguesa")
    print("2. Papas fritas")
    print("3. Refresco")
    print("4. Helado")
    print("5. Big Mac")

bienvenida()

opcion = int(input("Elige una opcion: "))
print(auto_servicio(opcion))
