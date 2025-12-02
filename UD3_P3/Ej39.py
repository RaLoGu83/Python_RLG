import random

num = random.randint(1, 100)
intentos = 10
contador = 0

while intentos > 0:
    x = int(input("Número: "))
    contador += 1
    intentos -= 1
    if x == num:
        print("Acertaste en", contador, "intentos")
        break
    elif x < num:
        print("Mayor. Intentos restantes:", intentos)
    else:
        print("Menor. Intentos restantes:", intentos)

if intentos == 0 and x != num:
    print("No acertaste. El número era", num)
