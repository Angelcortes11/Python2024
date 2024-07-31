print("Este programa te pide 10 numeros y te devuelve los pares de la lista ")

numeros_pares = []

for i in range(10):
    numero = int(input("Ingrese un número: "))
   
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Los números pares ingresados son: ", numeros_pares)