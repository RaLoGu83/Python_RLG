ahorro_total = 0

for mes in range(1, 13):
    deposito = float(input(f"Depósito mes {mes}: "))
    ahorro_total += deposito
    print(f"Ahorro acumulado hasta el mes {mes}: {ahorro_total}")

print("Ahorro total al final del año:", ahorro_total)
