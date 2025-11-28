sueldo_base = int(input("Sueldo base: "))
ventas = int(input("Ventas realizadas: "))

comision = sueldo_base * 0.1
comisiones = comision * ventas
sueldo_total = comisiones + sueldo_base

print(f"El sueldo total será de: {sueldo_total}")