correo = input("Ingresa tu correo electrónico: ")
partes = correo.split("@")
nuevo_correo = partes[0] + "@ceu.es"
print(nuevo_correo)