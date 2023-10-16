"""
Inicio
Escribe "Introduce tu nombre"
Escribe "Introduce tu edad"
Leer edad, nombre
Si no existe nombre
    nombre = "Desconocido"
Mientras True:
    Si 0 < edad <125
        Escribir "Te llamas {nombre} y tienes {edad} años, te quedan aún {125-edad} años por cumplir"
        break
    Si no
        Escribir "Introduzca una edad comprendida entre 0 y 125 años."
Fin
"""
nombre = input("Introduce tu nombre: ")
if not nombre:
    nombre = "Desconocido"
while True:
    edad = int(input("Introduce tu edad: "))
    if edad > 0 and edad <= 125:
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125-edad} años por cumplir")
        break
    else:
        print("Introduzca una edad comprendida entre 0 y 125 años.")