"""
Inicio
	Escribe "Introduce dos números: "
	Lee n1
	Lee n2
	opcion = 0
	Mientras (opcion < 1 or opcion > 4) hacer
		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
		Lee opcion
		Si (opcion < 1 or opcion > 4) entonces
			Escribe "Error - No es una opción correcta (1-4)"
	Segun (opcion) entonces
		1:
			Escribe n1 + " + " + n2 + " = " + (n1+n2)
		2:
			Escribe n1 + " - " + n2 + " = " + (n1-n2)
		3:
			Escribe n1 + " * " + n2 + " = " + (n1*n2)
		4:
			Si (n2 == 0) entonces
				Escribe "La división por cero no es posible"
			Sino
				Escribe n1 + " / " + n2 + " = " + (n1/n2)
Fin
"""
num1 = input("Escribe un numero: ")
while(num1.isdigit() == False):
    num1 = input("Escribe un numero entero, no otra cosa: ")
num2 = input("Escribe otro numero: ")
while(num2.isdigit() == False):
    num2 = input("Escribe un numero entero, no otra cosa: ")
num3 = int(input("Escribe un numero: (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "))
while(num3 < 1 or num3 > 4):
    num3 = int(input("Escribe un numero entero: (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División), no otra cosa: "))
num1 = int(num1)
num2 = int(num2)
match num3:
    case 1:
        resultado = num1+num2
    case 2:
        resultado = num1-num2
    case 3:
        resultado = num1*num2
    case 4:
        if(num2 == 0):
            resultado = "La division por 0 no es posible"
        else:
            resultado = num1/num2
print(resultado)