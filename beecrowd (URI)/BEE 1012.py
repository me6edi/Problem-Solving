A,B,C = input().split()
a = float(A)
b = float(B)
c = float(C)
pi = 3.14159
triangulo = (a * c) / 2
circulo = pi * (c**2)
trapezio = ((a+b) / 2 )* c
quadrado = b * b
retangulo = a * b
print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)
