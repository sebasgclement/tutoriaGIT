def promedio(suma, cantidad):
    prom = suma / cantidad
    return prom

n1 = float (input("Ingrese la nota 1"))
n2 = float (input("Ingrese la nota 2"))
n3 = float (input("Ingrese la nota 3"))

acu = n1 + n2 + n3
print("El promedio de las notas es: ", promedio(acu,3))