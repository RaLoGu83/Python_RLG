d = int(input("Día: "))
m = int(input("Mes: "))
a = int(input("Año: "))

valida = True

if m < 1 or m > 12:
    valida = False
elif d < 1:
    valida = False
elif m in (1,3,5,7,8,10,12) and d > 31:
    valida = False
elif m in (4,6,9,11) and d > 30:
    valida = False
else:
    bisiesto = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
    if m == 2:
        if bisiesto and d > 29:
            valida = False
        elif not bisiesto and d > 28:
            valida = False

if valida:
    print("Fecha correcta")
else:
    print("Fecha incorrecta")
