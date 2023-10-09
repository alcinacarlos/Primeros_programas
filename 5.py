siniva = int(input("Precio sin IVA: "))
iva= int(input("Porcentaje IVA a aplicar (sin %): "))
print(f"Precio total: {round(siniva+siniva*(iva/100), 2)}€")