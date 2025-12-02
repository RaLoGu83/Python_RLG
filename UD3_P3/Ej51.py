total = 0
pago = 10

for mes in range(1, 21):
    print(f"Mes {mes}: {pago} euros")
    total += pago
    pago *= 2

print("Total pagado después de 20 meses:", total, "euros")
