class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def tieneSol(self):
        det = self.a * self.d - self.b * self.c
        return det != 0.0
    def getX(self):
        det = self.a * self.d - self.b * self.c
        if det != 0.0:
            return (self.e * self.d - self.b * self.f) / det
    def getY(self):
        det = self.a * self.d - self.b * self.c
        if det != 0.0:
            return (self.a * self.f - self.e * self.c) / det
class Main():
    t1 = EcuacionLineal(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
    if t1.tieneSol():
        print("x =", t1.getX(),",","y =", t1.getY())
    else:
        print("La ecuacion no tiene solucion")
    t2 = EcuacionLineal(1.0, 2.0, 2.0, 4.0, 5.0, 10.0)
    if t2.tieneSol():
        print("x =", t2.getX(),",","y =", t2.getY())
    else:
        print("La ecuacion no tiene solucion")