N = int(input("Número de empleados: "))
total_empresa = 0

for i in range(1, N + 1):
    horas = float(input(f"Horas trabajadas empleado {i}: "))
    pago_hora = float(input(f"Pago por hora empleado {i}: "))
    sueldo = horas * pago_hora
    total_empresa += sueldo
    print(f"Sueldo empleado {i}: {sueldo}")

print("Total pagado por la empresa:", total_empresa)
