trabajo1 = float(input("Nota trabajo 1: "))
trabajo2 = float(input("Nota trabajo 2: "))
trabajo3 = float(input("Nota trabajo 3: "))
examen_final = float(input("Nota examen final: "))
trabajo_final = float(input("Nota trabajo final: "))

media_trabajos = (trabajo1+trabajo2+trabajo3)/3

nota_final = media_trabajos*0.55 + examen_final*0.3+trabajo_final*0.15

print(f"La nota final es: {nota_final:.2f}")