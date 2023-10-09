importefinal = int(input("Importe final: "))
iva = 1.1
print(f"IVA pagado: {round(importefinal-importefinal/iva, 2)}€")
print(f"Producto sin IVA: {round(importefinal/iva, 2)}€")