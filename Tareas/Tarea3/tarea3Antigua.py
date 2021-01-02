import estructura

#persona: id_usuario (str), lugares_visitados (dict)
estructura.mutable("usuario", "id_usuario lugares_visitados")


listaUsuarios = []



# Funciones Auxiliares ######

def crearUsuario(id_usuario, lugares_visitados):
    return usuario(id_usuario, lugares_visitados)

###########################################################

# cargarUbicacionesALista: str -> none
# recibe un string con la dirección de la base de datos a analizar, y modifica la 
# lista global recopilando en estructuras usuario cada usuario y sus respectivos lugares visitados.
# Ejemplo:  cargarUbicacionesALista(ejemplo.txt) llena la listaGlobal con [usuario(jperez, {mercado1:12, feria2:11})... ]
def cargarUbicacionesALista(archivo):
    
    ## Lectura de archivo ##
    A = open(archivo, "r")
    #Itero sobre las lineas del archivo 
    for entrada in A:

        #Quita el line break
        entrada = entrada.strip()

        #Separo por comas la linea
        instanciaUsuario = entrada.split(",")

        id_usuario = instanciaUsuario[0]
        lugar  = instanciaUsuario[1]
        hora   = int(instanciaUsuario[2])

        # Por si se quieren los usuarios ordenados alfabeticamente, descomentar esta linea
        #listaUsuarios.sort(key=lambda x: x.id_usuario)

        listaUsuarios.append(usuario(id_usuario, {lugar:hora}))


        for usuarioN in listaUsuarios:
            if usuarioN.id_usuario == id_usuario:
                usuarioN.lugares_visitados.update({lugar:hora})

                #Se eliminan duplicados
                for usuarioPrima in listaUsuarios:
                    if usuarioPrima.id_usuario == usuarioN.id_usuario and usuarioPrima != usuarioN:
                        listaUsuarios.pop(listaUsuarios.index(usuarioPrima))
        
    A.close()


def indiceId(id_usuario):
    # Busco usuario en lista
    for usuario in listaUsuarios:
        if usuario.id_usuario == id_usuario:
            return listaUsuarios.index(usuario)
    
    # Si no existe, retorno -1
    return -1

#print(indiceId("jperez"))


def contactoEstrecho(usuario1, usuario2):
    if usuario1 == usuario2:
        #print("¡Error: Se ha ingresado el mismo usuario!")
        return False    #No sé muy bien que retornar acá. HAY QUE VER ESTO

    lugares1 = usuario1.lugares_visitados
    lugares2 = usuario2.lugares_visitados

    for lugar in lugares1:
        if lugar in lugares2:
            # Si las horas son iguales
            if lugares1[lugar] == lugares2[lugar]:
                return True 
            continue
        
    return False



def imprimeContactosEstrechosEntre(usuario1, usuario2):
    
    salida = ""
    
    if not contactoEstrecho(usuario1, usuario2):
        return usuario1.id_usuario + " no ha tenido contactos estrechos con " + usuario2.id_usuario
    
    lugares1 = usuario1.lugares_visitados
    lugares2 = usuario2.lugares_visitados

    for lugar in lugares1:
        if lugar in lugares2:
            # Si las horas son iguales
            if lugares1[lugar] == lugares2[lugar]:
                salida = salida + usuario1.id_usuario + " coincidió con " + usuario2.id_usuario + " en " + lugar + " a las " + str(lugares1[lugar]) + " horas." + "\n"

    return salida
    


def imprimeContactosEstrechosDe(id_sospechoso):
    
    # Por si algún identifiacor es sólo un número REVISAR ESTO CON AYUDANTE
    id_sospechoso = str(id_sospechoso)

    # Opero sobre una lista idéntica, para evitar modificar la lista global
    listaSinUsuario = listaUsuarios.copy()

    if indiceId(id_sospechoso) == -1:
        return print("No se registran movimientos para el usuario " + id_sospechoso)

    salidaSinContactos = "El usuario " + id_sospechoso + " no ha tenido contactos estrechos."
    contacto = False

    # En caso de que no hayan contactos estrechos, para que la comparación no se rompa,
    # creo este usuario fake que nunca puede dar true en la comparación
    usuarioSospechoso = crearUsuario(id_sospechoso, {"EsteEsUnLugarFake":-1 })

    # Búsqueda de usuario en lista global
    for usuarioN in listaSinUsuario:
        if usuarioN.id_usuario == id_sospechoso:
            usuarioSospechoso = crearUsuario(id_sospechoso, usuarioN.lugares_visitados) 

    #Saco al sospechoso de la comparacion
    listaSinUsuario.pop(listaSinUsuario.index(usuarioSospechoso))

    for usuarioN in listaSinUsuario:
        if contactoEstrecho(usuarioSospechoso, usuarioN):
            print("Contacto estrecho " + usuarioN.id_usuario + "\n" + imprimeContactosEstrechosEntre(usuarioSospechoso, usuarioN))
            contacto = True

    if not contacto:
        print(salidaSinContactos)

 



#imprimeContactosEstrechosDe("rmunoz")
#print(contactoEstrecho(listaUsuarios[0], listaUsuarios[1]))


#print(imprimeContactosEstrechosEntre(listaUsuarios[0], listaUsuarios[3]))





# Rutina del programa ##############################################################

print("Sistema trazador de contactos COVID19")

#Dirección del archivo que contiene los datos a analizar
ubicacionDatos = input("Ingrese el nombre el archivo de ubicaciones: ")
cargarUbicacionesALista(ubicacionDatos)
print("Archivo " + ubicacionDatos + " cargado a lista \n")


def rutinaPrograma():

    id_sospechoso = input("Ingrese el identificador de la persona sospechosa de COVID (o 'fin'): ")
    print("")

    if id_sospechoso == "fin":
        return print("Gracias por usar el Sistema Trazador de Contactos COVID19.")

    imprimeContactosEstrechosDe(id_sospechoso)

    #Recursividaddadadaadadadadadadadad
    rutinaPrograma()

rutinaPrograma()

# Fin de rutina #########################################################################