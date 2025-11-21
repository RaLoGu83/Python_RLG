Trabajador = input("Ingrese el nombre del trabajador: ")
HTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
TNormal = float(input("Ingrese la tarifa por hora normal: "))

if HTrabajadas <= 35:
    SalarioBruto = TNormal * HTrabajadas
else:
    HorasExtra = HTrabajadas - 35
    SalarioBruto = (35 * TNormal) + (HorasExtra * TNormal * 1.5)

Impuesto = 0

if SalarioBruto > 900:
    Impuesto += (SalarioBruto - 900) * 0.45
    Impuesto += 400 * 0.25
elif SalarioBruto > 500:
    Impuesto += (SalarioBruto - 500) * 0.25

SalarioNeto = SalarioBruto - Impuesto

print(f"\n===== RESULTADOS =====")
print(f"Trabajador: {Trabajador}")
print(f"Salario bruto: {SalarioBruto:.2f}€") #:.2f redondea a 2 decimales
print(f"Impuestos aplicados: {Impuesto:.2f}€")
print(f"Salario neto: {SalarioNeto:.2f}€")
