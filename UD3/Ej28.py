n = 100
pares = 0
impares = 0

while n < 200:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    n += 1

print(f"La cantidad de números pares entre 100 y 200 es: {pares}")
print(f"La cantidad de números impares entre 100 y 200 es: {impares}")
