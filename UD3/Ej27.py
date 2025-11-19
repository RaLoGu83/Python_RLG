nota = 0
contador = 0
contador10 = 0
while nota != -1:
    nota = int(input("Ingrese la nota del estudiante (0-10): "))
    contador += 1
    if nota == 10:
        contador10 += 1
    elif nota <0 or nota > 10:
        print("Nota inválida")
    elif nota == -1:
        print("Finalizando entrada de notas.")
    else:
        continue

print(f"La cantidad de notas ingresadas es: {contador - 1}")
print(f"La cantidad de notas con 10 es: {contador10}")