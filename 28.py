"""
Inicio

Escribe "Introduce un número entero"
Escribe "Introduce otro número entero distinto"
Leer num1, num2
Si num1 == num2
     Escribe "No pueden ser ambos numeros iguales"
Si no
    Si num1>num2 entonces
        restantes = num1-num2
        Escribe El número menor es el {num2} y entre ellos existen {restantes} números enteros
    Si no
        restantes = num2-num1
        Escribe El número menor es el {num1} y entre ellos existen {restantes} números enteros
Fin
"""
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero distinto: "))
if num1 == num2:
    print("No pueden ser ambos numeros iguales")
else:
    if num1>num2:
        restantes = num1-num2
        print(f"El número menor es el {num2} y entre ellos existen {restantes} números enteros")
    else:
        restantes = num2-num1
        print(f"El número menor es el {num1} y entre ellos existen {restantes} números enteros")