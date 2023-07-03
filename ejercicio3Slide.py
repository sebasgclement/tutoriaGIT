# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Obtener la palabra invertida utilizando slicing
palabra_invertida = palabra[::-1]

# Verificar si la palabra ingresada es igual a su versión invertida
if palabra == palabra_invertida:
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")
