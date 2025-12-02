a = int(input("Inicio: "))
b = int(input("Fin: "))

for n in range(min(a, b), max(a, b) + 1):
    if n % 2 == 0:
        print(n)
