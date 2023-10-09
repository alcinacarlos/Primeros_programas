productos = input("Ingresa los productos de tu cesta de la compra separados por comas: ")
listaproductos = productos.split(",")
print("Productos en la cesta de la compra:")
for i in listaproductos:
    print(i.strip())