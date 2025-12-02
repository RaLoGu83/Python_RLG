N = int(input("Número de empleados: "))
total_empresa = 0

for i in range(1, N + 1):
    dias = int(input(f"Días trabajados empleado {i}: "))
    horas_totales = 0
    for d in range(1, dias + 1):
        horas = float(input(f"Horas trabajadas día {d}: "))
        horas_totales += horas
    pago_hora = float(input(f"Pago por hora empleado {i}: "))
    sueldo = horas_totales * pago_hora
    total_empresa += sueldo
    print(f"Sueldo semanal empleado {i}: {sueldo}")

print("Total pagado por la empresa:", total_empresa)
