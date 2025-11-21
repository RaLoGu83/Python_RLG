cantidad = int(input("Introduce una cantidad en euros (múltiplo de 5): "))

if cantidad % 5 != 0:
    print("La cantidad debe ser múltiplo de 5.")
else:
    billetes = [500, 200, 100, 50, 20, 10, 5]
    print("Descomposición mínima en billetes:")

    for b in billetes:
        num_billetes = cantidad // b
        if num_billetes > 0:
            print(f"{num_billetes} billetes de {b}€")
        cantidad %= b