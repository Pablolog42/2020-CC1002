import random

#codificaJugada: string -> int
#Asigna un código numerico a cada palabra a jugar. En caso de no ser válida la entrada, retorna -1.
#Ej: codificaJugada(tijeras) -> 0
def codificaJugada(jugada):
	if jugada == "tijeras":
		codigo = 0
	elif jugada == "papel":
		codigo = 1
	elif jugada == "piedra":
		codigo = 2
	elif jugada == "lagarto":
		codigo = 3
	elif jugada == "spock":
		codigo = 4
	else:
		codigo = -1

	return codigo


assert codificaJugada("tijeras") == 0
assert codificaJugada("papel") == 1
assert codificaJugada("lagarto") == 3
assert codificaJugada("miau soy un gatito que hace miauuuu") == -1	# tests de codificaJugada


#decodificaJugada: int -> string
#Inversa de "codificaJugada()", toma el código numerico y lo asigna a la palabra correspondiente. 
#En caso de código invalido retorna un string vacío
#Ej: codificaJugada(tijeras) -> 0
def decodificaJugada(codigo):
	if codigo == 0:
		jugada = "tijeras"
	elif codigo == 1:
		jugada = "papel"
	elif codigo == 2:
		jugada = "piedra"
	elif codigo == 3:
		jugada = "lagarto"
	elif codigo == 4:
		jugada = "spock"
	else:
		jugada = ""

	return jugada

assert decodificaJugada(1) == "papel"	
assert decodificaJugada(2) == "piedra"
assert decodificaJugada(3) == "lagarto"
assert decodificaJugada(-1) == ""	# tests de decodificaJugada


#codificaJugada: int, int -> int
#Analiza dos jugadas y retorna 1 si gana J1, 2 -1 si gan J2, 0 si hay empate y 42 si los argumentos son jugadas inváidas
#Ej: ganaJugada(0, 4) -> -1
def ganaJugada(jug_1, jug_2):
	if jug_1 == jug_2:  # Caso Empate
		salida = 0

	# Caso Gana 1 -> valor de salida = 1
	# Subcaso 0: J1 juega tijeras
	elif jug_1 == 0 and (jug_2 == 1 or jug_2 == 3):
		salida = 1

	# Subcaso 1: J1 juega papel
	elif jug_1 == 1 and (jug_2 == 2 or jug_2 == 4):
		salida = 1

	# Subcaso 2: J1 juega piedra
	elif jug_1 == 2 and (jug_2 == 3 or jug_2 == 0):
		salida = 1

	# Subcaso 3: J1 juega lagarto
	elif jug_1 == 3 and (jug_2 == 4 or jug_2 == 1):
		salida = 1

	# Subcaso 4: J1 juega spock
	elif jug_1 == 4 and (jug_2 == 2 or jug_2 == 0):
		salida = 1


	# Caso Gana 2 -> valor de salida = -1
	# Subcaso 0: J2 juega tijeras
	elif jug_2 == 0 and (jug_1 == 1 or jug_1 == 3):
		salida = -1

	# Subcaso 1: J2 juega papel
	elif jug_2 == 1 and (jug_1 == 2 or jug_1 == 4):
		salida = -1

	# Subcaso 2: J2 juega piedra
	elif jug_2 == 2 and (jug_1 == 3 or jug_1 == 0):
		salida = -1

	# Subcaso 3: J2 juega lagarto
	elif jug_2 == 3 and (jug_1 == 4 or jug_1 == 1):
		salida = -1

	# Subcaso 4: J2 juega spock
	elif jug_2 == 4 and (jug_1 == 2 or jug_1 == 0):
		salida = -1
	
	# Caso error (si se escribe algo que no es válido)
	elif jug_1 == -1 or jug_2 == -1:
		salida = 42	# https://www.youtube.com/watch?v=8190ziL5v-k

	return salida

assert ganaJugada(0, 4) == -1	# Tests de ganaJugada:
assert ganaJugada(2, 2) == 0
assert ganaJugada(2, 0) == 1
assert ganaJugada(-1, 0) == 42


#justificaJugada: int, int -> string
# Retorna la frase "jugada 1 + verbo + jugada2", donde verbo es la justificación de porqué gana la jugada1 sobre jugada 2
#Ej: justificaResultado(0,1) -> "tijeras cortan papel"
def justificaResultado(jug_1, jug_2):

	# Caso 0 Tijeras... a
	if jug_1 == 0:
		if jug_2 == 1:
			verbo = "cortan"  
		else:
			verbo = "decapitan"

	# Caso 1 papel... a
	elif jug_1 == 1:
		if jug_2 == 2:
			verbo = "cubre" 
		else:
			verbo = "refuta"

	# Caso 2 piedra... a
	elif jug_1 == 2:
		if jug_2 == 3:
			verbo = "aplasta" 
		else:
			verbo = "destruye"	
		
	# Caso 3 lagarto... a
	elif jug_1 == 3:
		if jug_2 == 4:
			verbo = "envenena"
		else:
			verbo ="come"

	# Caso 4 Spock... a
	elif jug_1 == 4:
		if jug_2 == 2:
			verbo = "vaporiza"
		else:
			verbo = "destruye"

	return decodificaJugada(jug_1) + " " + verbo + " " + decodificaJugada(jug_2)

assert justificaResultado(0, 1) == "tijeras cortan papel"	
assert justificaResultado(3, 4) == "lagarto envenena spock"
assert justificaResultado(2, 3) == "piedra aplasta lagarto"	# tests de justificaResultado

#generaJugadaComputador: no recibe argumentos y retorna int
# Retorna uin entero aleatorio entre 0 y 4 (incluyente)
#Ej: generaJugadaComputador() -> 3
def generaJugadaComputador():
	rand = random.randint(0, 4)
	return rand

assert 0 <= generaJugadaComputador() <= 4	#Tests generaJugadaComputador()

