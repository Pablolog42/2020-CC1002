

#agenda: dict (nombre:fono)

# Agenda para testeo
agenda1 = {"Andres":22234646,"Maria":98723456,"David":43335555}


#buscar: str dict -> int (o None si no esta)
#buscar nombre en agenda y devolver fono
#ej: buscar("c",agenda)->1
def buscar(nombre,agenda):
    assert type(agenda)==dict and type(nombre)==str
    if nombre in agenda:
        return agenda[nombre]
    else:
        return None 

#agregar: str int dict -> none
# Agrega una entrada nombre:número a la agenda seleccionada
# Ej: agregar("Juan Radrigán", 42282271, {"Messi:424242"}) = {"Messi":424242, "Juan Radrigán":42282271}
def agregar(nombre, fono, agenda):
    assert type(agenda)==dict and type(nombre)==str and type(fono) == int
    agenda[nombre] = fono

#Tests
agregar("Juan Radrigán", 42282271, agenda1)
assert agenda1 == {'Andres': 22234646, 'Maria': 98723456, 'David': 43335555, 'Juan Radrigán': 42282271}

#borrar: str dict -> none
# Borra una entrada nombre:número de la agenda seleccionada. Si no existe retorna error.
# Ej: borrar("Messi", {"Messi":424242, "Juan Radrigán":42282271}) = {"Messi:424242"}
def borrar(nombre, agenda):
    assert type(agenda)==dict and type(nombre)==str
    if nombre in agenda:
        del agenda[nombre]
    else:    
        return print("Error: No existe la entrada " + nombre + " en la agenda." ) 

#tests
borrar("Juan Radrigán", agenda1)
assert agenda1 == {"Andres":22234646,"Maria":98723456,"David":43335555}

borrar("Andres", agenda1)
assert agenda1 == {"Maria":98723456,"David":43335555}

# cambiarNumero: str int dict -> none
# Borra una entrada nombre:número sobreescribiendo el numero anterior con el indicado. Si no existe esa entrada tira error.
# Ej: cambiar_numero("Messi", 101010, {"Messi":424242}) = {"Messi:101010"}
def cambiar_numero(nombre, fonoNuevo, agenda):
    assert type(agenda)==dict and type(nombre)==str and type(fonoNuevo) == int
    if nombre in agenda:
        agenda[nombre] = fonoNuevo
    else:
        return print("Error: No existe la entrada " + nombre + " en la agenda." ) 

#tests
cambiar_numero("Maria", 303456, agenda1)
assert agenda1 == {"Maria":303456,"David":43335555}

cambiar_numero("David", 190238102838291309, agenda1)
assert agenda1 == {"Maria":303456,"David":190238102838291309}

