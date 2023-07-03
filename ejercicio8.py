# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Solicitar al usuario una longitud
longitud = int(input("Ingresa una longitud: "))

# Dividir la frase en palabras
palabras = frase.split()

# Inicializar el contador de palabras de longitud específica
contador_palabras = 0

# Iterar sobre cada palabra en la lista
for palabra in palabras:
    # Verificar si la longitud de la palabra coincide con la longitud específica
    if len(palabra) == longitud:
        # Incrementar el contador de palabras
        contador_palabras += 1

# Imprimir el resultado
print("En la frase hay", contador_palabras, "palabras de longitud", longitud)
