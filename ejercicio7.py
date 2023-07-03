# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Crear una lista para almacenar los caracteres únicos
caracteres_unicos = []

# Iterar sobre cada caracter de la palabra
for caracter in palabra:
    # Verificar si el caracter ya está en la lista de caracteres únicos
    if caracter not in caracteres_unicos:
        # Agregar el caracter a la lista de caracteres únicos
        caracteres_unicos.append(caracter)

# Construir la palabra sin caracteres repetidos utilizando la lista de caracteres únicos
palabra_sin_repetidos = ''.join(caracteres_unicos)

# Imprimir la palabra sin caracteres repetidos
print("Palabra sin caracteres repetidos:", palabra_sin_repetidos)
