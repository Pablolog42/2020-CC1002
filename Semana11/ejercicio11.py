
# __Cola: list(any) 
class Queue:

    #constructor de clase
    def __init__(self):
        self.__Cola = [] # una lista vacía es el caso base

    # empty: none -> bool
    # retorna True si la cola esta vacía
    def empty(self):
        return self.__Cola == []

    #enque: any -> none
    # efecto: agrega un elemento al final de la cola
    def enque(self, valor):
        self.__Cola.append(valor) # Agrega al ultimo elemento que llega al ultimo de cola

    #deque: none -> any
    # efecto: Quita de la cola al elemento que va en la cabecera y lo retorna
    def deque(self):
        return self.__Cola.pop(0) #Saca al primero de la cola

    #reset: none -> none
    # efecto: Resetea la cola (elimina todos los elementos)
    def reset(self):
        self.__Cola.clear() 

#Tests 
cola1 = Queue()

#método empty
assert cola1.empty()
cola1.enque("Primer elemento")
assert not cola1.empty()


cola1.enque(2)
cola1.enque(["Soy el tercer elemento"])

# Assert deque (FIFO)
assert cola1.deque() == "Primer elemento" 
assert cola1.deque() == 2

cola1.reset()
assert cola1.empty()

