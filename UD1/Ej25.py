nota = float(input("Introduce una calificación numérica (0-10): "))

while nota < 0 or nota > 10:
    print("La calificación debe estar entre 0 y 10")
    nota = float(input("Introduce una calificación numérica (0-10): "))

if nota < 3:
    calificacion = "Muy Deficiente"
elif nota < 5:
    calificacion = "Insuficiente"
elif nota < 6:
    calificacion = "Suficiente"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print(f"La calificación {nota} corresponde a: {calificacion}")