while True:
    inf = float(input("Límite inferior: "))
    sup = float(input("Límite superior: "))
    if inf < sup:
        break

suma = 0
fuera = 0
igual_limite = False

while True:
    n = float(input("Número: "))
    if n == 0:
        break
    if inf < n < sup:
        suma += n
    elif n < inf or n > sup:
        fuera += 1
    if n == inf or n == sup:
        igual_limite = True

print("Suma dentro del intervalo:", suma)
print("Números fuera del intervalo:", fuera)
print("Se introdujo algún número igual a los límites:", igual_limite)
