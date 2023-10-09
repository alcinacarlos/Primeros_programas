barra = 3.49
descuento = 0.60
nofrescas = int(input("Ingrese el número de barras no frescas vendidas: "))
totalnofrescas = nofrescas * barra * (1 - descuento)
print(f"Barra de pan: {barra:.2f} €")
print(f"Descuento por no ser fresca: {descuento * 100:.0f}%")
print(f"Costo total de las barras no frescas: {totalnofrescas:.2f} €")
