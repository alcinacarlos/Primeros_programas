"""
Inicio
Escribir "Número de inicio: "
Escribir "Incremento: "
Escribir "Total serie: "
Leer inicio, incremento, total_serie
resultado = "Serie=> " + inicio + -
contador = 1
Mientras incremento<=0 hacer
    Escribir "El incremento tiene que ser mayor que 0"
    Leer incremento
Mientras total_serie<=0 hacer
    Escribir "El total de la serie tiene que ser mayor que 0"
    Leer total_serie
Mientras(contador <= total_serie)
    resultado += ".." + inicio+incremento*contador
    contador += 1
Escribir resultado
Fin
"""
inicio = int(input("Número de inicio: "))
incremento = int(input("Incremento: "))
total_serie = int(input("Total serie: "))
resultado = "SERIE => " + str(inicio)+ "-"
contador = 1
while(incremento<=0):
    print("El incremento tiene que ser mayor que 0")
    incremento = int(input("Incremento: "))
while(total_serie<=0):
    print("El total de la serie tiene que ser mayor que 0")
    total_serie = int(input("Total serie: "))
while(contador <= total_serie-2):
    resultado += str(inicio+incremento*contador)
    contador += 1
    if (contador < total_serie-1):
        resultado += ".."
resultado += "-" + str(inicio+incremento*contador)
print(resultado)