total_horas = 0
pago_por_hora = float(input("Pago por hora: "))

for dia in range(1, 7):
    horas = float(input(f"Horas trabajadas día {dia}: "))
    total_horas += horas

sueldo = total_horas * pago_por_hora
print("Total de horas trabajadas:", total_horas)
print("Sueldo a recibir:", sueldo)
