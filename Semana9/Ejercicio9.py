# formatear: list[str] -> list[str]
#Recibe una lista con nombres mal formateados (con mayusculas/ minusculas cambiadas).
#Ordena la lista y arregla el formato de todos los nombres para que queden: Nombre Apellido
# Ej: formatear(["erneSto SabatO", "juan radrigan"]) = ["Ernesto Sabato", "Juan Radrigan"]

def formatear(nombres):

    listaMinusculas = []
    listaCapitalizada = []
    listaFormateada = []

    # Minúsculas
    for nombre in nombres:
        nombreMinusculas = nombre.lower()
        listaMinusculas.append(nombreMinusculas)
    # Ordenar
    listaMinusculas.sort()

    #Primera Mayuscula
    for nombre in listaMinusculas:
        nombreCapitalizado = nombre[0].upper() + nombre[1:len(nombre)]  # La mayuscula y el resto
        listaCapitalizada.append(nombreCapitalizado)    #lo agrego a la lista capitalizada

    #Segunda Mayuscula (Esto está más feo que feín pero funciona JAJAJAJAJ)
    for nombre in listaCapitalizada:
        for n in range(len(nombre)):
            if nombre[n] == " ":
                nombreFormateado = nombre[0:n+1] + nombre[n+1].upper() + nombre[n+2:len(nombre)]  # Lo de antes + Capital Apellido + lo de después
                listaFormateada.append(nombreFormateado)

    return listaFormateada

#Tests
assert formatear(["erneSto SabatO", "juan radrigan"]) == ["Ernesto Sabato", "Juan Radrigan"]
assert formatear(['XimEna OlivOS','Claudia GoMez', 'Maria Smith','andrea Pinto','jorge rodriguez', 'peDro orTuzar', 'BEATRIZ OH']) == ['Andrea Pinto', 'Beatriz Oh', 'Claudia Gomez', 'Jorge Rodriguez', 'Maria Smith', 'Pedro Ortuzar', 'Ximena Olivos']

