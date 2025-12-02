n = int(input("Cantidad: "))
may = men = cer = 0

for _ in range(n):
    x = float(input("Número: "))
    if x > 0:
        may += 1
    elif x < 0:
        men += 1
    else:
        cer += 1

print("Mayores que 0:", may)
print("Menores que 0:", men)
print("Iguales a 0:", cer)
