#Cristian Aguirre
#24-03-25
#Estoy Aburrido ✌️🍀

tareas = ['🏦 Sacar dinero del banco',
        '🍸 Hacer la colada',
        '💈 Cortarse el pelo',
        '☕ Preparar un té',
        '💻 Terminar el capitulo de Listas',
        '❤️ Llamar a mamá',
        '📺 Ver mi Hero Academia']

#1. Acceder a la primera tarea de la lista
print(tareas[0])

#2. Encontrar la segunda tarea de la lista 
print(tareas[1])

#3 Obtener un subconjunto de tareas usando slicing
print(tareas[2:4])

#Intentar Acceder a un indice inexistente y manejar el error
indice = 8
try:
    print(tareas[indice])

except IndexError:
    print('Esta Tarea aun no existe')

#5 Nueva Tarea

nueva_tarea = '🎮Jugar Valorant'

# Agrega 'nueva_tarea' al final de 'tareas'

tareas = tareas + [nueva_tarea]
print(tareas)

