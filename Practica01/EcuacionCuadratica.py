import math
class EcuacionCuadratica():
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDis(self):
        return self.__b**2 - 4*self.__a*self.__c
    def getRaiz1(self):
        d = self.getDis()
        if d >= 0:
            return (-self.__b + math.sqrt(d)) / (2*self.__a)
        else:
            return 0
    def getRaiz2(self):
        d = self.getDis()
        if d >= 0:
            return (-self.__b - math.sqrt(d)) / (2*self.__a)
        else:
            return 0

class Main():
    #Ecuacion 1
    e1 = EcuacionCuadratica(1, 3, 1)
    d = e1.getDis()
    if d > 0:
        print("La ecuacion tiene dos raices",
              format(e1.getRaiz1(), ".6f"),
              "y",
              format(e1.getRaiz2(), ".6f"))
    #Ecuacion 2
    e2 = EcuacionCuadratica(1, 2, 1)
    d = e2.getDis()
    if d == 0:
        print("La ecuacion tiene una raiz",
              format(e2.getRaiz1(), ".0f"))
    #Ecuacion 3
    e3 = EcuacionCuadratica(1, 2, 3)
    d = e3.getDis()
    if d < 0:
        print("La ecuacion no tiene raices reales")