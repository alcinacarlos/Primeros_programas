num = int(input("Introduce un número entero: "))
def suma_todos_enteros(numero):
    return f"La suma de todos los enteros desde 1 hasta {num} es: {int((numero*(numero+1))/2)}"

print(suma_todos_enteros(num))