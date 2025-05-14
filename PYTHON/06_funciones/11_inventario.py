#cristianoooooooooooooooooooooooooooooooooooooooooooooooooooo

inventario = []

def agregar_producto(producto):
    inventario.append(producto)
    print(f"Producto {producto} agregado al inventario.")

def ver_inventario():
    print('Inventario Actual:')
    for item in inventario :
        print(f"- {item}")
    
def eliminar_producto(producto):
    if producto in inventario:
        inventario.remove(producto)
        print(f"Producto {producto} eliminado del inventario.")
    else:
        print(f"El producto {producto} no se encuentra en el inventario.")

def buscar_producto(producto):
    if producto in inventario:
        print(f"El producto {producto} se encuentra en el inventario.")
    else:
        print(f"El producto {producto} no se encuentra en el inventario.")

agregar_producto("Laptop")
agregar_producto("Mouse")
agregar_producto("Teclado")
ver_inventario()

eliminar_producto("Mouse")
ver_inventario()

buscar_producto("Laptop")
buscar_producto("Monitor")
buscar_producto("Teclado")