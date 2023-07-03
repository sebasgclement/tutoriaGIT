# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Solicitar al usuario una subcadena
subcadena = input("Ingresa una subcadena: ")

# Inicializar el contador de apariciones de la subcadena
contador_apariciones = 0

# Obtener la longitud de la subcadena
longitud_subcadena = len(subcadena)

# Iterar sobre la frase utilizando un bucle while
indice = 0
while indice <= len(frase) - longitud_subcadena:
    # Obtener una porción de la frase del mismo tamaño que la subcadena
    porcion = frase[indice:indice+longitud_subcadena]
    
    # Verificar si la porción es igual a la subcadena
    if porcion == subcadena:
        # Incrementar el contador de apariciones
        contador_apariciones += 1
    
    # Avanzar al siguiente índice
    indice += 1

# Imprimir el resultado
print("La subcadena", subcadena, "aparece", contador_apariciones, "veces en la frase.")
