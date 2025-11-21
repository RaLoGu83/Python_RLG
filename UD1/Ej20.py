N = int(input("Introduce un número: "))

Factorial = 1
if N > 0:
    for i in range(1, N + 1):
        Factorial *= i

print(f"El factorial de {N} es: {Factorial}")
