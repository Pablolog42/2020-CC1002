import estructura
from lista import *
from abb import *

estructura.crear("lista", "valor siguiente")
estructura.crear("AB","valor izq der")


abb=AB("F",\
    AB("B",\
        AB("A",None,None),\
        AB("D",\
            AB("C",None,None),\
            AB("E",None,None))),\
    AB("G",\
        None,\
        AB("I",\
            AB("H", None, None),\
            None)))  

A=AB(59,\
    AB(5,\
        AB(1,None,None),\
        AB(8,\
            AB(7,None,None),\
            AB(50,None,None))),\
    AB(70,\
        None,\
        AB(200,\
            AB(105, None, None),\
            None)))  


L = lista(150, lista(10, lista(2, listaVacia)))

#listaAabb lista(any) abb -> abb

def listaAabb(L, A):

    x = cabeza(L)

    if x < A.valor:
        return AB(A.valor, insertar(x, A.izq), A.der)
    if x > A.valor:
        return AB(A.valor, A.izq, insertar(x, A.der))

print(listaAabb(L,A))

#abbAlista: abb  -> lista(any)

def escribir(arbol):
    assert arbol==None or type(arbol)==AB

    if arbol==None: 
        return 
    
    escribir(arbol.izq)
    lista1 = lista(arbol.valor, listaVacia)
    escribir(arbol.der)

print(escribir(abb))

#escribir: AB -> None
#escribir valores de ABB A en orden ...
#ej: escribir(abb) -> ...

# def escribir(arbol):
#     assert arbol==None or type(arbol)==AB
#     if arbol==None: 
#         return 
    
#     escribir(arbol.izq)
#     lista1 = lista(arbol.valor, listaVacia)
#     escribir(arbol.der)


#     return lista1


# print(escribir(abb))