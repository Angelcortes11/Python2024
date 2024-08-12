def menu():
    menuInicio = '''
      ::::::::::::::::::::::::::::::::::::::::::::
    #     1 - Añadir una tarea                 #
    #     2 - Ver todas las tareas             #
    #     3 - Marcar una tarea como completada #
    #     4 - Salir                            #
    .......................................... '''
    print(menuInicio)
    opcion = int(input("ingrese la opcion seleccionada: "))
    return opcion
    
diccionario = {}
opcion = menu()

def agregar_tarea(agenda):
    while True: 
        if opcion == 1:
            tarea = input("Ingrese el nombre de la tarea y su descripcion: ")
            tarea.append (tarea)
            print("tarea agregada correctamente.")

        elif opcion == 2:
            print("{agregar_tarea}")

        elif opcion == 3:
            print("¿Qué numero de tarea quieres marcar como completada?" "{agregar_tarea}")

        elif opcion == 4:
            print("Gracias por utilizar este programa")
            break
        else:
            print("fin por error en la eleccion de las opciones")

print("fin")
