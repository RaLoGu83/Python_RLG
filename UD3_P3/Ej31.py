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
    elif mes == 2:
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

alumnos = int(input("Número de alumnos: "))

if alumnos >= 100:
    costo_por_alumno = 65
    pago_compania = alumnos * costo_por_alumno
elif alumnos >= 50:
    costo_por_alumno = 70
    pago_compania = alumnos * costo_por_alumno
elif alumnos >= 30:
    costo_por_alumno = 95
    pago_compania = alumnos * costo_por_alumno
else:
    pago_compania = 4000
    costo_por_alumno = pago_compania / alumnos

print("Pago a la compañía de autobuses:", pago_compania, "euros")
print("Cada alumno debe pagar:", costo_por_alumno, "euros")
