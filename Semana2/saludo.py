import saludoFunciones

hora = int(input("Indique la hora: "))

if saludoFunciones.buenosDias(hora):
    print("¡Buen día!")
elif saludoFunciones.buenasTardes(hora):
    print("¡Buenas tardes!")
else:
    print("¡Buenas Noches!")
