Trabajador = input("Ingrese el nombre del trabajador: ")
HTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
TNormal = int(input("Ingrese la tarifa por hora normal: "))
SalarioBruto = 0
SalarioNeto = 0

if HTrabajadas <= 35:
    SalarioBruto = TNormal * HTrabajadas
    
elif HTrabajadas > 35:
    HorasExtra = HTrabajadas - 35
    SalarioBruto = (HorasExtra * TNormal * 1.5) + (35 * TNormal)
    
else:
    print("Error en la cantidad de horas trabajadas")
    
    
if SalarioBruto > 500 and SalarioBruto <= 900:
    Impuesto1 = SalarioBruto - 400
    SalarioNeto = SalarioBruto - (Impuesto1 * 0.25)
    print(f"Impuesto aplicado: {Impuesto1 * 0.25}€")
    
elif SalarioBruto > 900:
    Impuesto1 = 400 * 0.25
    Impuesto2 = SalarioBruto - 900
    SalarioNeto = SalarioBruto - Impuesto1 - (Impuesto2 * 0.45)
    print(f"Impuesto aplicado: {Impuesto1 + (Impuesto2 * 0.45)}€")

else:
    SalarioNeto = SalarioBruto

print(f"El salario bruto de {Trabajador} es: {SalarioBruto}€")
print(f"El salario neto de {Trabajador} es: {SalarioNeto}€")
