num = 0
contdiez = 0

while num != -1:
    num = int(input("Introduce número del uno al diez: "))

    if num < -1 or num > 10:
        print("Número no válido")
    elif num == 10:
        contdiez += 1
    else:
        continue
print(f"Has registrado 10: {contdiez} veces")