#crsitian Aguirre

#solicitar al usuario el numero del mes 

mes = int(input("ingrese el numero del mes: "))

#determinar la estacion usando if, elif y else

if mes == 1 or mes == 2 or mes == 3:
    print("invierno")
elif mes == 4 or mes == 5 or mes == 6:
    print("primavera")
elif mes == 7 or mes == 8 or mes == 9:
    print("verano")
elif mes == 10 or mes == 11 or mes == 12:
    print("otoño")
else:
    print("Invalid")

    