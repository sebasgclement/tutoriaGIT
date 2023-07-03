# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Utilizar el método split() para dividir la frase en palabras
palabras = frase.split()

# Obtener la cantidad de palabras
cantidad_palabras = len(palabras)

# Imprimir el resultado
print("La frase contiene", cantidad_palabras, "palabras.")
