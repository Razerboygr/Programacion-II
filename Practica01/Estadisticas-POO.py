import math
def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)
def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for i in range(len(lista)):
        suma += (lista[i] - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))

numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
prom = promedio(numeros)
desv = desviacion(numeros)
print("El promedio es", format(prom, ".2f"))
print("La desviacion estandar es", format(desv, ".5f"))