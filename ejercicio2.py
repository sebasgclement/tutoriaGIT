# Solicitar al usuario una frase
frase = input("Ingresa una frase: ")

# Inicializar una cadena vacía para almacenar la frase invertida
frase_invertida = ""

# Iterar sobre cada caracter de la frase en orden inverso
for i in range(len(frase)-1, -1, -1):
    # Agregar el caracter actual a la frase invertida
    frase_invertida += frase[i]

# Imprimir la frase invertida
print("Frase invertida:", frase_invertida)
