"""
Inicio
	Escribe "Dame 3 números: "
	Lee n1
	Lee n2
	Lee n3
	numeros = [n1, n2, n3]
	numeros.sort()
	Para num en numeros hacer
		resultado += num + " "
	Escribir resultado
Fin
"""
print("Dame 3 números: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
resultado = "Tus números son: "
numeros = [num1, num2, num3]
numeros.sort()
for num in numeros:
	resultado += str(num) + " "
print(resultado)