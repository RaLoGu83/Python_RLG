nota = int(input("Nota: "))
edad = int(input("Edad: "))
sexo = str(input("Sexo (m/f): "))
sexo = sexo.lower()

if nota >= 5 and edad >= 18 and sexo == "f":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "m":
    print("POSIBLE")
else:
    print("NO ACEPTADA")