capital_inicial = float(input("Ingrese la cantidad de dinero depositada: "))
interes = 0.04
primer = capital_inicial * (1 + interes)
segundo = primer * (1 + interes)
tercer = segundo * (1 + interes)
print(f"Primer año: {round(primer, 2)}€")
print(f"Segundo año: {round(segundo, 2)}€")
print(f"Tercer año: {round(tercer, 2)}€")