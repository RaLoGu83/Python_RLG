# altura = int(input("Introduce la altura de la pirámide: ")) 
# cadena = "*"
# espacios = " "

# for i in range (1, altura + 1):
#     cadena = cadena + "*"
#     espacios = " " * (altura - i)
#     cadena = "*" * (2 * i - 1)
#     print(espacios + cadena)


altura = int(input("Introduce la altura de la pirámide: "))

for i in range(1, altura + 1):
    for j in range(altura - i):
        print(" ", end="")
    for k in range (1,2*i):
            print("*", end="")
    print("")