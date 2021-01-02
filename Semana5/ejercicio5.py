import estructura
from lista import *

#suma: lista(int) -> int
#Suma todos los digitos de una lista de largo arbitrario
#Ej: suma(lista(1, lista(6, lista(3, listaVacia)) == 10
def suma(lista):
    # Solo recibo listas con enteros o vacias
    assert(vacia(lista) or type(cabeza(lista)) == int)

    # La suma de nada es el neutro aditivo
    if vacia(lista):
        return 0

    resultado = cabeza(lista)   

    # Caso base: lista de largo 1: lista(n, listaVacia)
    if cola(lista) == listaVacia:
        return resultado #Se retorna sólo la cabeza

    # Caso recursivo: 
    else:
        resultado += suma(cola(lista))  #Se suma recursivamente la cabeza de la lista actual con las siguientes 
        return resultado
        

#Tests
assert(suma(lista(1, lista(6, lista(3, lista(3, lista(3, listaVacia)))))) == 16) 
assert(suma(lista(0, lista(0, lista(0, lista(0, lista(0, listaVacia)))))) == 0) 
assert(suma(lista(0, lista(0, lista(0, lista(1, lista(-1, listaVacia)))))) == 0) 
assert(suma(lista(1, lista(6, lista(3, listaVacia)))) == 10) # 1+6+3
assert(suma(listaVacia)) == 0


