pi = 3.1416

radio = float(input("Ingrese la longitud del radio: "))

diametro = 2 * radio
longitud_circunferencia = pi * diametro
area_circulo = pi * (radio ** 2)
volumen_esfera = (4 / 3) * pi * (radio ** 3)

print(f"\nResultados para un radio de {radio}:")
print(f"Longitud de la circunferencia: {longitud_circunferencia}")
print(f"Área del círculo: {area_circulo}")
print(f"Volumen de la esfera: {volumen_esfera}")