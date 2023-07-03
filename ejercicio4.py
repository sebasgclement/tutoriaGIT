# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Inicializar el contador de palabras
contador_palabras = 1

# Iterar sobre cada caracter de la frase
for caracter in frase:
    # Verificar si el caracter es un espacio en blanco
    if caracter == ' ':
        # Incrementar el contador de palabras
        contador_palabras += 1

# Imprimir el resultado
print("La frase contiene", contador_palabras, "palabras.")
