# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Solicitar al usuario una subcadena
subcadena = input("Ingresa una subcadena: ")

# Utilizar el método count() para contar las apariciones de la subcadena en la frase
contador_apariciones = frase.count(subcadena)

# Imprimir el resultado
print("La subcadena", subcadena, "aparece", contador_apariciones, "veces en la frase.")
