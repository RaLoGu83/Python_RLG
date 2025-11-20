contpos = 0
contneg = 0

for i in range (100, 200):

    if i % 2 == 0:
        contpos += 1
    else:
        contneg += 1
print(f"Hay {contpos} positivos")
print(f"Hay {contneg} negativos")