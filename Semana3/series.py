# potencia: num int -> num
# calcula el valor de una potencia de base elevado a exponente
# para exponentes enteros positivos
# ejemplo: potencia (4,5) debe dar 1024
def potencia(a, b):
    assert (type(b)==int) and b >= 0

    if b == 0:  # Caso Base
        return 1
    else:
        return potencia(a, b-1) * a 
#Tests
assert potencia(4, 5) == 1024
assert potencia(0, 10) == 0 #Test caso especial
assert potencia(10, 0) == 1 #Test caso base



#serieGeometrica: int -> num
#Calcula la sumatoria de 1/(2^i) hasta i=n
#ej: serieGeometrica(5) debe ser 1.96875
def serieGeometrica(n):
    assert (type(n)==int) and n >= 0
    
    if n == 0:  # Caso Base
        return 1
    else:
        return serieGeometrica(n-1) + 1/potencia(2, n)
#Tests
assert serieGeometrica(5) == 1.96875
assert serieGeometrica(1) == 1.5
assert serieGeometrica(0) == 1  #Test caso base