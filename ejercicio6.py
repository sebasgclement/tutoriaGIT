# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Convertir la palabra a minúsculas para facilitar la comparación
palabra = palabra.lower()

# Inicializar el contador de vocales
contador_vocales = 0

# Iterar sobre cada caracter de la palabra
for caracter in palabra:
    # Verificar si el caracter es una vocal
    if caracter in "aeiou":
        # Incrementar el contador de vocales
        contador_vocales += 1

# Imprimir el resultado
print("La palabra contiene", contador_vocales, "vocales.")
