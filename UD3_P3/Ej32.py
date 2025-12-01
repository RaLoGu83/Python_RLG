dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

fecha_correcta = True

if mes < 1 or mes > 12:
    fecha_correcta = False
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:  
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28
    
    if dia < 1 or dia > max_dias:
        fecha_correcta = False

if fecha_correcta:
    print("La fecha es correcta.")
else:
    print("La fecha NO es correcta.")


minutos = int(input("Minutos de la llamada: "))
dia_semana = input("¿Fue domingo? (s/n): ").lower()
turno = "ninguno"

if dia_semana != "s":
    turno = input("Turno (mañana/tarde): ").lower()

costo = 0

if minutos <= 5:
    costo = 1
elif minutos <= 8:
    costo = 1 + (minutos - 5) * 0.80
elif minutos <= 10:
    costo = 1 + (3 * 0.80) + (minutos - 8) * 0.70
else:
    costo = 1 + (3 * 0.80) + (2 * 0.70) + (minutos - 10) * 0.50

if dia_semana == "s":
    impuesto = costo * 0.03
else:
    if turno == "mañana":
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10

total = costo + impuesto

print("Costo base de la llamada: ", round(costo, 2), "euros")
print("Impuesto:", round(impuesto, 2), "euros")
print("Total a pagar:", round(total, 2), "euros")
