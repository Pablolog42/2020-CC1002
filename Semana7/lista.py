import estructura

# Diseno de la estructura
# lista : valor (any = cualquier tipo) siguiente (lista)
estructura.crear("lista", "valor siguiente")

# identificador para listas vacias
listaVacia = None

# crearLista: any lista -> lista
# devuelve una lista cuya cabeza es valor
# y la cola es resto
def crearLista(valor, resto):
        return lista(valor, resto)

# cabeza: lista -> any
# devuelve la cabeza de una lista (un valor)
def cabeza(lista): 
	return lista.valor

# cola: lista -> lista
# devuelve la cola de una lista (una lista)
def cola(lista):
	return lista.siguiente

# vacia: lista -> bool
# devuelve True si la lista esta vacia
def vacia(lista):
	return lista == listaVacia

# unionListas: lista(any) lista(any) -> lista(any)
# devuelve lista resultado de unir dos listas
# ejemplo: unionListas(lista(1, listaVacia), lista(2, listaVacia)) 
# devuelve lista(1, lista(2, listaVacia))
def unionListas(lista1, lista2):
    if vacia(lista1):
        return lista2
    else:
        return lista(cabeza(lista1), unionListas(cola(lista1), lista2))

# Test
unaLista = lista(1, listaVacia)
otraLista = lista(2, lista(3, listaVacia))
assert unionListas(unaLista, otraLista) == lista(1, lista(2, lista(3, listaVacia)))


# Tests

test_lista = lista(1, lista(2, lista(3, listaVacia)))

assert cabeza(test_lista) == 1
assert cabeza(cola(test_lista)) == 2
assert cabeza(cola(cola(test_lista))) == 3
assert cola(cola(test_lista)) == lista(3, listaVacia)

assert vacia(listaVacia)
assert not vacia(test_lista)
assert vacia(cola(cola(cola(test_lista))))

