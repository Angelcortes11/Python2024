tareas = []

while True:
    opcion = input("Añadir una tarea (a), Ver todas las tareas (v), Marcar una tarea como completada (c), Salir (s): ")
 
    if opcion == "a":
        tareas.append(input("Nueva tarea: "))

    elif opcion == "v":
        print("Tareas:", tareas)

    elif opcion == "c":
        tareas.pop(int(input("Número de tarea completada: ")) - 1)

    elif opcion == "s":
        print("Gracias por utilizar este programa")
        break
    else:
        print("fin por error en la eleccion de las opciones")

print("fin")
