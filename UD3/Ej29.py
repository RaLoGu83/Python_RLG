print("Piensa en un número entre 1 y 100")

minimo = 1
maximo = 100

while True:
    adivino = (minimo + maximo) // 2
    print(f"\nCreo que tu número es: {adivino}")
    respuesta = input("¿Es mayor (m), menor (n) o igual (i)?: ")

    if respuesta == "i":
        print(f"\nFacilito.")
        break
    elif respuesta == "m":
        minimo = adivino + 1
    elif respuesta == "n":
        maximo = adivino - 1
    else:
        print("Respuesta no válida. Por favor escribe 'm', 'n' o 'i'.")