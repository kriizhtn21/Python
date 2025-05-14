#Cristian Aguirre
#4/14/25
#enfasi

altura = int(input("cual es tu altura (cm): "))


creditos = int(input("cuantos creditos tienes: "))

altura_suficiente = altura >= 137
creditos_suficientes = creditos >= 10

if altura_suficiente and creditos_suficientes:
    print("disfruta tu viaje")
elif altura_suficiente and not creditos_suficientes:
    print("puedes disfrutar el viaje pero no puedes llevar a nadie contigo")

else:
    print("lo sentimos, la atraccion esta cerrada en este momento")
    