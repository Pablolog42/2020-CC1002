#buenosDias: int -> bool
#Recibe una hora del dia y dice si corresponde a la mannana o no (entre 1<=x<12)
#Ej: buenosDias(12) devuelve False

def buenosDias(hora):
    if (1 <= hora < 12):
        return True
    else:
        return False    

#buenasTardes: int -> bool
#Recibe una hora del dia y dice si corresponde a la tarde o no (entre 12<=x < 21)
#Ej: buenasTardes(13) devuelve true
def buenasTardes(hora):
    if ( 12 <= hora < 21):
        return True
    else:
        return False


#Tests
assert buenosDias(12) == False
assert buenasTardes(24) == False
assert buenasTardes(12) == True
assert buenosDias (1) == True
    