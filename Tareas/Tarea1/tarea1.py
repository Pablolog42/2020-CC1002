import random
from cachipunLS import *

#Funciones Auxiliares

#textoIntro: no recibe argumentos, retorna strings
#Escribe la introducción al juego en pantalla
#Ej: textoIntro() devuelve "Bienvenido al juego del cachipún-lagarto-spock... "
def textoIntro():
	print("Bienvenido al juego del cachipún-lagarto-spock!!!")
	print("Ingrese la modalidad en que quiere jugar")
	print("jugador vs. computador (1) o computador vs. computador (2):")

#jugador_v_computador: no recibe argumentos, retorna bool
#Inicia la rutina de juego en modalidad 1 (Jugador vs PC) y retorna un booleano que indica si hubo empate
#Ej: jugador_v_computador() devuelve True (Empate)
def jugador_v_computador():
	print("Modalidad elegida: Jugador vs. Computador")
	print("Jugador 1 ingrese jugada ['papel'|'tijeras'|'piedra'|'lagarto'|'spock']:")
	
	empate = False # Artículo 4 Código Procesal penal: Todo empate es falso hasta que se demuestre lo contrario

	jug_1 = codificaJugada(input())
	jug_2 = generaJugadaComputador()

	print("Jugador 2 (computador) juega " + decodificaJugada(jug_2))

	# Caso gana J1
	if ganaJugada(jug_1, jug_2) == 1:
		justificacion = justificaResultado(jug_1, jug_2)
		print("Gana Jugador 1!! " + justificacion)
	# Caso	gana J2
	elif ganaJugada(jug_1, jug_2) == -1:
		justificacion = justificaResultado(jug_2, jug_1)
		print("Gana Jugador 2!! " + justificacion)
	# Caso Empate (Devuelve bool empate)
	elif ganaJugada(jug_1, jug_2) == 0:
		empate = True
		print("Empate!")

	# Caso Error
	elif ganaJugada(jug_1, jug_2) == 42:
		print("Error: Jugada inválida")
	
	return empate

#computador_v_computador: no recibe argumentos, retorna bool
#Inicia la rutina de juego en modalidad 1 (PC vs PC) y retorna un booleano que indica si hubo empate
#Ej: jugador_v_computador() devuelve False (No hay empate)
def computador_v_computador():
	print("Modalidad elegida: Computador vs. Computador")

	jug_1 = generaJugadaComputador()
	jug_2 = generaJugadaComputador()

	empate = False # Artículo 4 Código Procesal penal: Todo empate es falso hasta que se demuestre lo contrario

	print("Jugador 1 (computador) juega " + decodificaJugada(jug_1))
	print("Jugador 2 (computador) juega " + decodificaJugada(jug_2))

	# Caso gana J1
	if ganaJugada(jug_1, jug_2) == 1:
		justificacion = justificaResultado(jug_1, jug_2)
		print("Gana Jugador 1!! " + justificacion)
	# Caso	gana J2
	elif ganaJugada(jug_1, jug_2) == -1:
		justificacion = justificaResultado(jug_2, jug_1)
		print("Gana Jugador 2!! " + justificacion)
	# Caso Empate
	elif ganaJugada(jug_1, jug_2) == 0:
		empate = True
		print("Empate!")
		
	return empate




# Inicio del Juego #################################################

#juego:() no recibe argumentos ni retorna nada. Se usa unicamente para permitir la recursividad.
#Inicia la rutina principal del juego. Se utiliza además para recursividad en caso de empate
#Ej: juego() parte el juego xD
def juego():

    textoIntro() 

    modalidad = int(input()) # 1: jvsC 2: CvsC

    if modalidad == 1:
        empate = jugador_v_computador()      # Retonrna True si hay empate

    elif modalidad == 2:
        empate = computador_v_computador()   # Idem

    else:
        print ("Modalidad invalida!")


    if empate:
        print("¿Desea jugar nuevamente? (si/no)")
        respuesta = input()

        if respuesta == "si" or respuesta == "Si":
            juego() #Se reinicia recursivamente el juego
        else:
            print("¡Gracias por Jugar!")

juego()

# https://bit.ly/3bPBpZo ###########################################





