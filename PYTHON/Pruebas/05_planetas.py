#cristiano

#solicitar el peso terrestre del usuario
peso_terrestre = float(input("Introduce tu peso en la Tierra: "))

#solicitar el numero del planeta

planeta = int(input("Introduce el número del planeta (1-7): "))

#calcular el peso en el planeta correspondiente

if planeta == 1:
    peso_destino = peso_terrestre * 0.38 #mercurio
    print(f"Tu peso en mercurio seria :{peso_destino:.2f} kg")
elif planeta == 2:
    peso_destino = peso_terrestre * 0.91 #venus
    print(f"Tu peso en venus seria :{peso_destino:.2f} kg")
elif planeta == 3:
    peso_destino = peso_terrestre * 0.38 #marte
    print(f"Tu peso en marte seria :{peso_destino:.2f} kg")
elif planeta == 4:
    peso_destino = peso_terrestre * 2.34 #jupiter
    print(f"Tu peso en jupiter seria :{peso_destino:.2f} kg")
elif planeta == 5:
    peso_destino = peso_terrestre * 1.06 #saturno
    print(f"Tu peso en saturno seria :{peso_destino:.2f} kg")
elif planeta == 6:
    peso_destino = peso_terrestre * 0.92 #urano
    print(f"Tu peso en urano seria :{peso_destino:.2f} kg")
elif planeta == 7:
    peso_destino = peso_terrestre * 1.19 #neptuno
    print(f"Tu peso en neptuno seria :{peso_destino:.2f} kg")
else:
    print("Numero de planeta no valido")