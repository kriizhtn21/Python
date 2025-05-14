#cristianooooo

#definir la calificacion comoun numero decimal

rating = float(input("Ingrese el rating del restaurante (0-5:)"))

#Sistema de calificacion

if rating > 4.5:
    print("Extraordinario")
elif rating > 4:
    print("Excelente")
elif rating > 3:
    print("Bueno")
elif rating > 2:
    print("Regular")    
else:
    print("Pesimo")
    