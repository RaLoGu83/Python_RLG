import time

horas = int(input("Horas iniciales: "))
minutos = int(input("Minutos iniciales: "))
segundos = int(input("Segundos iniciales: "))

while True:
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    time.sleep(1)
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
