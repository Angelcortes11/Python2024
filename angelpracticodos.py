frase = input("Ingrese una frase: ")
contador_vocales = 0
for caracter in frase:
    if caracter in "aeiouAEIOU":
        contador_vocales += 1

print("La frase ingresada contiene", contador_vocales, "vocales.")