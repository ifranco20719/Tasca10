def sumar(a): # Definim la funció de sumar
		suma = 0
		for i in a:
			suma += i
		return suma
def multiplicació(a): # Definim la funció de multiplicar
		multiplicar = 1
		for i in a:
			multiplicar *=i
		return multiplicar
x = [1, 1, 1, 1]
print("La suma de tots els elements de la llista és: ", sumar(x))
print("La multiplicació de tots els elements de la llista és: ", multiplicació(x))
