num = int(input("Introduce un número entero: "))
def suma_todos_enteros(numero):
    return (numero*(numero+1))/2

print(f"La suma de todos los enteros desde 1 hasta {num} es: {suma_todos_enteros(num)}")