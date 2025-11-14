altura = int(input("Introduce la altura de la pirámide: ")) 
cadena = "*"
espacios = " "

for i in range (1, altura + 1):
    cadena = cadena + "*"
    espacios = " " * (altura - i)
    cadena = "*" * (2 * i - 1)
    print(espacios + cadena)