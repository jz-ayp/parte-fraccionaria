"""
Determinar si un número tiene parte fraccionaria
"""

# Entradas
numero = float(input("Introduzca un número: "))
	
# Proceso
if numero == int(numero):
	resultado = "no"
else:
	resultado = "sí"

	
# Salidas
print("El número", numero, resultado, "tiene parte fraccionaria.")
