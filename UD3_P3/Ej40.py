s = 0
c = 0
while True:
    n = float(input("Número: "))
    if n == 0:
        break
    s += n
    c += 1

print("Suma:", s)
print("Media:", s / c if c > 0 else 0)
