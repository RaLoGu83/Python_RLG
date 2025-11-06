PA = int(input("Introducir precio del artículo: "))
PV = int(input("Introducir precio de la venta: "))

Descuento = (PA - PV) / PA * 100
print("El descuento aplicado es de: ", Descuento, "%")