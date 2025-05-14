#xoro cristian
#14/5/25
#enfasi
#1:45 AM

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

print(fibonacci_recursivo(10))  # Salida: 55
# 55 es el resultado de la secuencia de Fibonacci para n=10

#pedimos al usuario un numero
n = int(input("ingrese un numero: "))

#mostramos la secuencia hasta el numero ingresado
for i in range(n):
    print(fibonacci_recursivo(i))