# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Inicializar una variable para almacenar la palabra invertida
palabra_invertida = ""

# Iterar sobre cada caracter de la palabra en orden inverso
for i in range(len(palabra)-1, -1, -1):
    # Agregar el caracter actual a la palabra invertida
    palabra_invertida += palabra[i]

# Verificar si la palabra ingresada es igual a su versión invertida
if palabra == palabra_invertida:
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")
#Probando modificar un archivo 
#Segundo comentario 
