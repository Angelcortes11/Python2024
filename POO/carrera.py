from Personaje_clase import Personaje

print("Este programa es para que el usuario decida la media de cada atributo de un personaje")

personajes = []

while True:
    opcion = input("Añadir altura (a), Añadir velocidad (v), Añadir resistencia (r), Añadir fuerza (f), ver todos los atributos (va), Salir (s): ")

    if opcion == "a":
        personajes.append(input(" altura: "))

    elif opcion == "v":
        personajes.append(input(" velocidad: "))

    elif opcion == "r":
          personajes.append(input(" resistencia: "))

    elif opcion == "f":
          personajes.append(input(" fuerza: "))

    elif opcion == "va":
          print("Atributos del personaje: ", personajes )

    elif opcion == "s":
        print("Gracias por utilizar este programa")
        break
    else:
        print("fin por error en la eleccion de las opciones")
   
    p1 = Personaje("Superman", 120, 75, 69, 100)
print (f"el personaje se llama {p1.nombre} y cuenta con los atributos de: " , personajes)


print("fin")


