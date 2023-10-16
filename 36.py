"""
Inicio
Escribir "¿Cuántas notas vas a introducir?: "
Leer num_notas
contador = 0
media = 0
Mientras numeros_notas < 1 O numeros_notas > 100
    Escribir "Error - el número de notas debe ser un número entero entre 1 y 100"
    Escribir "¿Cuántas notas vas a introducir?: "
    Leer numros_notas
Escribir "Dame las {numeros_notas} notas del curso: "
Mientras contador!= numeros_notas
    Escribir ""
    Leer num
    media += num
    contador += 1
Escribit La media es de media/numeros_notas
Fin
"""
numeros_notas = int(input("¿Cuántas notas vas a introducir?: "))
contador = 0
media = 0
while(numeros_notas < 1 or numeros_notas > 100):
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    numeros_notas = int(input("¿Cuántas notas vas a introducir?: "))
print(f"Dame las {numeros_notas} notas del curso: ")
while(contador != numeros_notas):
    num = int(input())
    media += num
    contador += 1
print("La media es de", round(media/numeros_notas,2))