# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Inicializar el contador de letras
contador_letras = 0

# Iterar sobre cada caracter de la palabra
for caracter in palabra:
    # Verificar si el caracter es una letra
    if caracter.isalpha():
        # Incrementar el contador de letras
        contador_letras += 1

# Imprimir el resultado
print("La palabra", palabra, "contiene", contador_letras, "letras.")
