numero = int(input("Introduce el número obtenido en el dado (1-6): "))

if numero < 1 or numero > 6:
    print("ERROR: número incorrecto.")
else:
    if numero == 1:
        opuesta = 6
    elif numero == 2:
        opuesta = 5
    elif numero == 3:
        opuesta = 4
    elif numero == 4:
        opuesta = 3
    elif numero == 5:
        opuesta = 2
    else:  
        opuesta = 1

    if opuesta == 1:
        letra = "uno"
    elif opuesta == 2:
        letra = "dos"
    elif opuesta == 3:
        letra = "tres"
    elif opuesta == 4:
        letra = "cuatro"
    elif opuesta == 5:
        letra = "cinco"
    else:  
        letra = "seis"

    print("La cara opuesta es:", letra)
