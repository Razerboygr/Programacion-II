import math
class Estadistica:
    def __init__(self, datos):
        self.__datos = datos
    def promedio(self):
        suma = 0
        for i in range(len(self.__datos)):
            suma += self.__datos[i]
        return suma / len(self.__datos)
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for i in range(len(self.__datos)):
            suma += (self.__datos[i] - prom) ** 2
        return math.sqrt(suma / (len(self.__datos) - 1))

class Main():
    numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
    est = Estadistica(numeros)
    print("El promedio es", format(est.promedio(), ".2f"))
    print("La desviacion estandar es", format(est.desviacion(), ".5f"))