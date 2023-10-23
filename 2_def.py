horas = int(input("Horas de trabajo: "))
coste = int(input("Coste por hora: "))
def importe_total(horas, coste):
    return f"Importe total: {horas*coste}"
print(importe_total(horas, coste))