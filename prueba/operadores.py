password = "123456"

# Contador de intentos
intentos = 0
imax = 3

# Pedir al usuario que ingrese la contraseña hasta 3 intentos
while intentos < imax:
    intento = input("Introduce la contraseña: ")
    if intento == password:
        print("¡Contraseña correcta!")
        break
    else:
        intentos += 1
        print(F"Contraseña incorrecta. Intento {intentos} de {imax} intentos")

    if intentos == 3:
        print("Has agotado tus intentos. Programa terminado.")
