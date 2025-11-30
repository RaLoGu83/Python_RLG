x = int(input("Introducir año: "))

if x%4 == 0:
    print(f"El año {x} es bisiesto")
else:
    print(f"El año {x} no es bisiesto")