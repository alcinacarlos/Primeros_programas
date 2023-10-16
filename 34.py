"""
Inicio
num = 3
contador = 1
Escribe "Numeros que tiene ue tener la serie: "
Leer num_serie
resultado = num
Mientreas contador != num_serie hacer
    contador += 1
    num += 3
    resultado += " " + num
Escribir resultad
Fin
"""
num_serie = int(input("Numeros que tiene ue tener la serie: "))
num = 3
contador = 1
resultado = str(num)
while(contador != num_serie):
    contador += 1
    num += 3
    resultado += " " + str(num)
print(resultado)