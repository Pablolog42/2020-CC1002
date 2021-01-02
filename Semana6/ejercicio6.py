import estructura
from lista import *
from abstraccion import *


# registro: producto(str) precio(int) cantidad(int) 
estructura.crear("producto", "nombre precio cantidad")


# Funcion para ocupar el fold
# sumaProductos: int producto -> int
# Suma a un valor base la ponderación del valor de un producto por su cantidad respectiva
# Ej: Si se compra un solo (valor = 0) "producto" con atributos "Album de Luis Jara" "1500" "1"
# la función retornará 1500 (que igual es como un poco caro para un album de Lucho Jara)
def sumaProductos(valor, producto):
    if vacia(producto):
        return 0
    else:
        precio = producto.precio
        cantidad = producto.cantidad

        valor += precio*cantidad
        return valor

# Tests sumaProductos
assert sumaProductos(0, producto("Miel Gibson", 1234, 0)) == 0 # No hay miel
assert sumaProductos(0, producto("Guafo", 15870000000, 1)) == 15870000000 # $$$$$



# totalCarrito: lista(producto) -> int
# Retorna la suma total de una lista carrito llena de productos
# Ej: totalCarrito(lista(producto("cafe", 2500, 3), lista(producto("aceite", 5000, 1), listaVacia))) retorna 12500
def totalCarrito(carrito):
    if vacia(carrito):
        return 0
    return fold(sumaProductos, 0, carrito)


# Tests totalCarrito
assert totalCarrito(lista(producto("cafe", 2500, 3), lista(producto("aceite", 5000, 1), listaVacia))) == 12500
assert totalCarrito(lista(producto("un té calentito", 1000, 1), lista(producto("fruta", 500, 4), lista(producto("pan", 100, 5), lista(producto("café", 2500, 1), listaVacia))))) == 6000
assert totalCarrito(listaVacia) == 0