import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = int(time.time() * 1000)
        self.__finaliza = 0
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = int(time.time() * 1000)
    def detener(self):
        self.__finaliza = int(time.time() * 1000)
    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia
    
class Main():
    def seleccion(lista):
        n = len(lista)
        for i in range(n - 1):
            minimo = i
            for j in range(i + 1, n):
                if lista[j] < lista[minimo]:
                    minimo = j
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux
    print("Ordenacion por seleccion de 100000 numeros")
    numeros = []
    for i in range(100000):
        numeros.append(random.randint(1, 100000))
    cron = Cronometro()
    cron.inicia()
    seleccion(numeros)
    cron.detener()
    print("Tiempo transcurrido:", cron.lapsoDeTiempo(), "milisegundos")