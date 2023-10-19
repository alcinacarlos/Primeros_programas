import concurrent.futures
def factorial(num:int):
    num_factorial = 1
    while(num != 0):
        num_factorial *= num
        num -= 1
    return num_factorial

def factorialStr(num:int):
    resultado = str(num) + "!"+ " => "
    num_factorial = 1
    while(num != 0):
        num_factorial *= num
        if(num-1 == 0):
            resultado += str(num) + " = "
        else:
            resultado += str(num)  + " x "
        num -= 1
    resultado += str(num_factorial)
    return resultado
numero = int(input("Introduce el numero: "))
print(factorialStr(numero))
print(factorial(numero))
