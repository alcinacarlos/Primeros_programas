sin_iva = int(input("Precio sin IVA: "))
iva_a_aplicar= int(input("Porcentaje IVA a aplicar (sin %): "))
def precio_con_iva(iva, siniva):
    print(f"Precio total: {round(siniva+siniva*(iva/100), 2)}€")
    
precio_con_iva(iva_a_aplicar, sin_iva)