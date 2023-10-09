producto = input("Por favor, ingresa el nombre del producto: ")
preciounitario = float(input("Ingresa el precio unitario del producto: "))
numerounidades = int(input("Ingresa el número de unidades: "))
costo_total = preciounitario * numerounidades
cadena_resultado = "{} - Precio Unitario: {:>9,.2f} - Número de Unidades: {:>3} - Costo Total: {:>11,.2f}".format(
    producto, preciounitario, numerounidades, costo_total
)
print(cadena_resultado)