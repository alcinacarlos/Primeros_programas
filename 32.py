"""
Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x >= y) entonces
		numIni = x
		numFin = y
	Sino
		numIni = y
		numFin = x
		
	Mientras (numIni <= numFin) hacer
		Escribe numIni
		Si (numIni != numFin) entonces
			Escribe "-"
                numIni = numIni + 1

Fin
"""
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
numini = min(num1, num2)
numfin = max(num1, num2)
resultado = ""
while(numini != numfin):
    resultado += str(numini) + "-"
    numini += 1
print(resultado + str(numfin))