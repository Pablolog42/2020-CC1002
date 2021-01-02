from estructura import *
from lista import *
from abstraccion import *
from estadisticas import *
import math

# resultadoMesa: circunscripcion (str), mesa (int), apruebo (int), rechazo (int)
estructura.crear("resultadoMesa", "circunscripcion mesa apruebo rechazo")


#Puchis esto no funca
# #contadorCircunscripciones(listaResultados): lista(resultadosMesa) -> int
# #retorna la cantidad de circunscripciones distintas que existen en una lista
# #Ej: contadorCircunscripciones(L, 0) == 3
# def contadorCircunscripciones(listaResultados, contador):
    
#     if vacia(listaResultados):
#         return 0   

#     #Caso Base
#     if vacia(cola(listaResultados)):
#         return contador

#     circunscipcion = cabeza(listaResultados).circunscripcion

#     #Si no existe la circunscipción, se agrega al contador
#     if not buscaCircunscipcion(cola(listaResultados), circunscipcion):
#         contador += 1
#         contadorCircunscripciones(cola(listaResultados), contador)
    
#     #Si ya existe, un berlini no le hace nadii 
#     contadorCircunscripciones(cola(listaResultados), contador)
    
    
#busquedaPorCircunscripcion: lista(resultadoMesa) -> none
#Ejecuta el buscador de la mesa de su interés. Al finalizar la ejecución
#escribiendo "fin", se rompe la ejecución devolviendo al usuario un mensaje
#de agradecimiento
def busquedaPorCircunscripcion(listaResultados):
    print("")
    circunscripcion = input("Circunscripción de su interés (o 'fin' para terminar): ")
    assert type(circunscripcion) == str

    #Fin de la ejecucion
    if circunscripcion == "fin":
        return print("¡Gracias por utilizar este programa!")
    
    #Si la circunc. ingresada no existe
    elif vacia(resultadosCircunscripcion(listaResultados, circunscripcion)):
        print("¡La circunscripción ingresada no está registrada!")
        busquedaPorCircunscripcion(listaResultados)

    totalApruebo = str(totalesPorCircunscripcion(listaResultados, circunscripcion, "apruebo"))
    totalRechazo = str(totalesPorCircunscripcion(listaResultados, circunscripcion, "rechazo"))
    print("Votación en Circunscripción " + circunscripcion + ":")
    print("Apruebo: " + totalApruebo + ", Rechazo: " + totalRechazo)

    #Recursividadadadadadadad
    busquedaPorCircunscripcion(listaResultados)

#estadistica: lista(resultadosMesa) -> lista(resultadosMesa)
#Ejecuta la rutina de estadistica de una lista de resultados electorales
# Devuelve la mesa más concurrida, el total de votos de apruebo y de rechazo
# Ej: estadistica(lista) devuelve "Estadisticas basicas: Totales plebiscito..."
def estadistica(listaResultados):
    print(" ")
    print("Estadísticas Básicas:")
    print("Totales Plebiscito Constituyente")

    totalApruebo = str(totalVotosFinales(listaResultados, "apruebo"))
    totalRechazo = str(totalVotosFinales(listaResultados, "rechazo"))

    print("Total Opción Apruebo: " + totalApruebo)
    print("Total Opción Rechazo: " + totalRechazo)
    print(" ")

    mesaMasConcurrida = mesaConMasVotos(listaResultados)
    circunscripcion = str(mesaMasConcurrida.circunscripcion)
    mesa = str(mesaMasConcurrida.mesa)
    votantes = str(mesaMasConcurrida.apruebo + mesaMasConcurrida.rechazo)
    #numeroDeCircunscripciones = str(contadorCircunscripciones(listaResultados, 0))

    print("Estadisticas Avanzadas: ")    
    print("Mesa con más concurrencia: " + circunscripcion + ", mesa " + mesa + ", con " + votantes + " votantes.")    

    return busquedaPorCircunscripcion(listaResultados)

#ingresaDatos: listaVacia -> lista(resultadosMesa)
#Ejecuta la rutina principal del programa. En caso de que el usuario indique que llegó al final,
#Ejecuta la rutina de estadisticas, enviando como parámetro la lista con lo que el usuario esribió
#Ej: ingresaDatos(listaVacia) = "Bienvenido al sistema de estadísticas Plebiscito Constituyente 2020... "
def ingresaDatos(listaResultados):
    print("Bienvenido al sistema de estadísticas Plebiscito Constituyente 2020.")
    print("Ingrese los resultados por mesa:")

    circunscripcion = str(input("Circunscripción (o ‘fin’ para terminar): "))
    
    #Ejecutar estadisticas acá. Esto rompe la recursividad.
    if circunscripcion == "fin":
        if vacia(listaResultados):
            return print("Error: ¡No hay datos que analizar!")
        return estadistica(listaResultados)

    mesa = input("Número de la mesa: ")
    assert type(mesa) == str #Para mesas únicas (Por ej. 94V)
    votosApruebo = int(input("Número de votos opción Apruebo: "))
    votosRechazo = int(input("Número de votos opción Rechazo: "))

    listaResultados = agregaMesa(listaResultados, resultadoMesa(circunscripcion, mesa, votosApruebo, votosRechazo))

    #Recursividaddadadaadadadadadadadad
    ingresaDatos(listaResultados)



# #Se ejecuta el programa
ingresaDatos(listaVacia)


    


