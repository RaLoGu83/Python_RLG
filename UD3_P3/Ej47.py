import math

n = int(input("Número: "))

if n < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            primo = False
            break

print("Primo" if primo else "No primo")
