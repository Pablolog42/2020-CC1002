# Nota importante:
# Se pone en los tests una desigualdad de rango muy pequeño en vez de una igualdad
# para compensar el error de aproximación al multiplicar floats

# Definición pi uwu
pi = 3.1415


# areaCirculo: float -> float
# calcula el área de un círculo de radio r
# Ej: areaCirculo(3) = 28.2735
def areaCirculo(r):
	return pi * r ** 2


assert 28.2734 < areaCirculo(3) < 28.2736  # Test areaCirculo


# perimetroCirculo: float -> float
# calcula el perimetro de un círculo de radio r
# Ej: areaAnillo(5, 2) =
def perimetroCirculo(r):
	return 2 * pi * r


assert 6.282 < perimetroCirculo(1) < 6.284  # Test perimetroCirculo


# areaAnillo: float, float -> float
# calcula el área de un anillo entre dos círculos de radios r_exterior, r_interior
# Ej: areaAnillo(5, 2) = 65.9715
def areaAnillo(r_exterior, r_interior):
	return areaCirculo(r_exterior) - areaCirculo(r_interior)


assert 65.9714 < areaAnillo(5, 2) < 65.9716  # Test areaAnillo


# perimetroAnillo: float, float -> float
# calcula el perimetro de un anillo entre dos círculos de radios r_exterior, r_interior
# Ej: perimetroAnillo(5, 2) = 43.981
def perimetroAnillo(r_exterior, r_interior):
	return perimetroCirculo(r_exterior) + perimetroCirculo(r_interior)


assert 43.980 < perimetroAnillo(5, 2) < 43.982  # Test perimetroAnillo
