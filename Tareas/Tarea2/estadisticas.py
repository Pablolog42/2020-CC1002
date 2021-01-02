import estructura
from lista import *
from abstraccion import *


# resultadoMesa: circunscripcion (str), mesa (int), apruebo (int), rechazo (int)
estructura.crear("resultadoMesa", "circunscripcion mesa apruebo rechazo")

#Resultados de ejemplo. Utilizados para los Assert.
r1 = resultadoMesa("temuco", 2,100,20)
r2 = resultadoMesa("Santiago", 2,100,70000)
r3 = resultadoMesa("pirque", 2,100,20)
r4 = resultadoMesa("temuco", 3,1500,500) # Grande Deportes Temuco

L2 = lista(resultadoMesa("pirque", "94V",100,20), None)


L = lista(r1, lista(r2, lista(r3, lista(r4, listaVacia))))
L1= lista(r1,listaVacia)


################################################ Funciones Auxiliares

#igualMesa: resultadoMesa resultadoMesa -> bool
# Compara dos valores resultadoMesa y retorna True si es que sus mesas son iguales.
#Ej: igualMesa(resultadoMesa("temuco", 2,100,20), resultadoMesa("temuco", 2,500,20)) == True
def igualMesa(r1, r2):
    if r1.circunscripcion != r2.circunscripcion:
        return False
    return r1.mesa == r2.mesa

#Tests igualMesa
assert igualMesa(resultadoMesa("temuco", 2,100,20), resultadoMesa("temuco", 2,500,20)) == True

#igualCircunscripcion: resultadoMesa resultadoMesa -> bool
# Compara dos valores resultadoMesa y retorna True si es que sus circunscripciones son iguales.
#Ej: igualCircunscripcion(resultadoMesa("temuco", 2,100,20), resultadoMesa("temuco", 30,500,20)) == True
def igualCircunscripcion(r1, r2):
    return r1.circunscripcion == r2.circunscripcion

#Tests igualCircunscripcion
assert igualCircunscripcion(resultadoMesa("temuco", 2,100,20), resultadoMesa("temuco", 40,500,20)) == True

#sumaVotosApruebo: int resultadoMesa -> int
#Toma un valor inicial de votos y un valor resultadoMesa, sumando al valor inicial los votos
#del apruebo de la mesa ingresada
#Ej: sumaVotosApruebo(0,resultadoMesa("temuco", 2,100,20) == 100
def sumaVotosApruebo(valor, resultadoMesa):
    votosApruebo = resultadoMesa.apruebo
    return valor + votosApruebo

#Tests sumaVotosApruebo
assert sumaVotosApruebo(0,resultadoMesa("temuco", 2,100,20)) == 100

#sumaVotosRechazo: int resultadoMesa -> int
#Toma un valor inicial de votos y un valor resultadoMesa, sumando al valor inicial los votos
#del rechazo de la mesa ingresada
#Ej: sumaVotosRechazo(0,resultadoMesa("temuco", 2,100,20)) == 20
def sumaVotosRechazo(valor, resultadoMesa):
    if vacia(resultadoMesa):
        return 0
    votosRechazo = resultadoMesa.rechazo
    return valor + votosRechazo

#Tests sumaVotosRechazo
assert sumaVotosRechazo(0,resultadoMesa("temuco", 2,100,20)) == 20

#sumaVotosMesa: resultadoMesa -> int
#Suma todos los votos de una mesa.
#Ej: sumaVotosMesa(resultadoMesa("temuco", 2,100,20)) == 120
def sumaVotosMesa(resultadoMesa):
    return sumaVotosApruebo(0, resultadoMesa) + sumaVotosRechazo(0, resultadoMesa)

#Tests sumaVotosMesa
assert sumaVotosMesa(resultadoMesa("temuco", 2,100,20)) == 120

#masVotos: resultadoMesa resultadoMesa -> resultadoMesa
#compara dos valores resultadoMesa y retorna el que tenga más votos
#ej: masVotos(resultadoMesa("temuco", 2,100,20),resultadoMesa("temuco", 3,2000,20)) == resultadoMesa("temuco", 3,2000,20)
def masVotos(r1, r2):
    if sumaVotosMesa(r1) > sumaVotosMesa(r2):
        return r1
    return r2

#Tests masVotos
assert masVotos(resultadoMesa("temuco", 2,100,20),resultadoMesa("temuco", 3,2000,20)) == resultadoMesa("temuco", 3,2000,20)


#buscaCircunscipcion: lista(resultadosMesa) str -> bool
# Ve si existe una circunscripción en la lista y retorna si es verdad esto o si es todo una cruel y vil falacia 
# ej: buscaCircunscripción(lista(resultadoMesa("temuco", 2,100,20), none),temuco) == True
def buscaCircunscipcion(listaResultados, circunscripcion):
    assert type(circunscripcion) == str
    assert type(cabeza(listaResultados)) == resultadoMesa

    # # Se genera un Resultado temporal solo valido para comparacion de circ. 
    resultadoLambda = resultadoMesa(circunscripcion, 0, 0,0)
    if vacia(filtro2(igualCircunscripcion, listaResultados, resultadoLambda)):
        return False
    return True

#Tests buscaCircunscripcion
assert buscaCircunscipcion(lista(resultadoMesa("temuco", 2,100,20), None), "temuco") == True
assert buscaCircunscipcion(L, "temuco") == True


################################################################### Funciones Pedidas


#buscaMesa: lista(resultadosMesa) str str -> resultadoMesa
# Busca un valor resultadoMesa dado en una lista dada y lo retorna 
#Ej: buscaMesa(L,"temuco",3) == resultadoMesa(circunscripcion='temuco', mesa=3, apruebo=1500, rechazo=500)
def buscaMesa(listaResultados, circunscripcion, mesa):
    assert type(circunscripcion) == str
    assert type(mesa) == int or type(mesa) == str
    #assert vacia(listaResultados) or type(cabeza(listaResultados)) == resultadoMesa
    # # Se genera un Resultado temporal solo valido para comparacion de circ. y mesa.
    resultadoLambda = resultadoMesa(circunscripcion, mesa, 0,0)
    if vacia(filtro2(igualMesa, listaResultados, resultadoLambda)):
        return listaVacia
    return cabeza(filtro2(igualMesa, listaResultados, resultadoLambda))

#Tests buscaMesa
assert buscaMesa(L,"temuco",3) == resultadoMesa(circunscripcion='temuco', mesa=3, apruebo=1500, rechazo=500)
assert buscaMesa(L,"Santiago",2) == resultadoMesa(circunscripcion='Santiago', mesa=2, apruebo=100, rechazo=70000)
assert buscaMesa(L2, "pirque", "94V")

#agregaMesa: lista(resultadosMesa) resultadoMesa  -> lista(resultadosMesa)
# Recibe una lista de resultadosMesa y un valor resultadoMesa. Agrega a la cabeza de la lista este ultimo valor
#Ej: agregaMesa() == lista(valor=resultadoMesa(circunscripcion='san javier', mesa=10, apruebo=100, rechazo=500), 
# siguiente=lista(valor=resultadoMesa(circunscripcion='temuco', mesa=2, apruebo=100, rechazo=20), siguiente=None))
def agregaMesa(listaResultados, resultadoMesaR):
    #assert vacia(listaResultados) or type(cabeza(listaResultados)) == resultadoMesa
    if vacia(filtro2(igualMesa, listaResultados, resultadoMesaR)):
        return lista(resultadoMesaR, listaResultados)
    return listaResultados

#Test Agrega Mesa
assert agregaMesa(L1,resultadoMesa("san javier", 10,100,500)) == lista(valor=resultadoMesa(circunscripcion='san javier', mesa=10, apruebo=100, rechazo=500), siguiente=lista(valor=resultadoMesa(circunscripcion='temuco', mesa=2, apruebo=100, rechazo=20), siguiente=None))
assert agregaMesa(L,resultadoMesa("temuco", 2,100,530)) == L #Esto deberia no modificar la lista


#resultadosCircunscripcion: lista(resultadosMesa) str  -> lista(resultadosMesa)
# Recibe una lista de resultadosMesa y una circunscripcion. 
# Retorna todos los resultadosMesa de una circunscripción especifica de una lista.
#Ej: resultadosCircunscripcion(L, "temuco") == lista(valor=resultadoMesa(circunscripcion='temuco', mesa=2, apruebo=100, rechazo=20), 
# siguiente=lista(valor=resultadoMesa(circunscripcion='temuco', mesa=3, apruebo=1500, rechazo=500), siguiente=None))
def resultadosCircunscripcion(listaResultados, circunscripcion):
    assert type(circunscripcion) == str
    #assert vacia(listaResultados) or type(cabeza(listaResultados)) == resultadoMesa
    # Se genera un Resultado temporal solo valido para comparacion de circ. y mesa. 
    resultadoLambda = resultadoMesa(circunscripcion, 0, 0, 0)
    if vacia(filtro2(igualCircunscripcion, listaResultados, resultadoLambda)):
        return listaVacia
    return filtro2(igualCircunscripcion, listaResultados, resultadoLambda)

#Tests resultadosCircunscripcion
assert resultadosCircunscripcion(L, "temuco") == lista(valor=resultadoMesa(circunscripcion='temuco', mesa=2, apruebo=100, rechazo=20), siguiente=lista(valor=resultadoMesa(circunscripcion='temuco', mesa=3, apruebo=1500, rechazo=500), siguiente=None))

#totalVotosFinales: lista(resultadosMesa) str  -> int
# Recibe una lista de resultadosMesa y una elección. 
# Retorna la suma de todos los votos de una elección especifica en una lista de resultadosMesa
#Ej: totalVotosFinales(L, "rechazo") == 70540
def totalVotosFinales(listaResultados, eleccion):
    assert type(eleccion) == str
    if vacia(listaResultados):
        return 0
    if eleccion == "apruebo":
        return fold(sumaVotosApruebo, 0, listaResultados)
    if eleccion == "rechazo":
        return fold(sumaVotosRechazo, 0, listaResultados)

#Tests totalVotosFinales
assert totalVotosFinales(L, "rechazo") == 70540

#totalesPorCircunscripcion: lista(resultadosMesa) str str -> int
# Recibe una lista de resultadosMesa, una circunscripción y una elección. 
# Retorna la suma de todos los votos de una circunscripción especifica en una lista de resultadosMesa
#Ej: totalesPorCircunscripcion(L, "rechazo") == 520
def totalesPorCircunscripcion(listaResultados, circunscripcion, eleccion):
    assert type(circunscripcion) == str
    assert type(eleccion) == str
    #assert vacia(listaResultados) or type(cabeza(listaResultados)) == resultadoMesa
    listaCircunscripcion = resultadosCircunscripcion(listaResultados, circunscripcion)
    return totalVotosFinales(listaCircunscripcion, eleccion)

#Tests totales por circunscripción
assert totalesPorCircunscripcion(L,"temuco", "rechazo") == 520


#mesaConMasVotos: lista(resultadosMesa) -> resultadoMesa
# Recibe una lista de resultadosMesa.
# Retorna el valor resultadoMesa con una mayor cantidad de votos totales
#Ej: mesaConMasVotos(L) == resultadoMesa(circunscripcion='Santiago', mesa=2, apruebo=100, rechazo=70000)
def mesaConMasVotos(listaResultados):
    #assert vacia(listaResultados) or type(cabeza(listaResultados)) == resultadoMesa
    if vacia(listaResultados):
        return None
    #Se genera resultado temporal que nunca exixtirá para el init.
    resultadoLambda = resultadoMesa("Rancagua no existe", -100, -100, -100)
    return fold(masVotos, resultadoLambda, listaResultados)

#Tests mesaConMasVotos
assert mesaConMasVotos(L) == resultadoMesa(circunscripcion='Santiago', mesa=2, apruebo=100, rechazo=70000)


