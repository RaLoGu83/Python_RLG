hora = int(input("Introduce la hora (0-23): "))
minuto = int(input("Introduce los minutos (0-59): "))
segundo = int(input("Introduce los segundos (0-59): "))

if segundo < 59:
    segundo += 1
elif minuto < 59:
    segundo = 0
    minuto += 1
else:
    segundo = 0
    minuto = 0
    hora = (hora + 1) % 24
horadespues = f"{hora:02}:{minuto:02}:{segundo:02}"
print(f"La hora transcurrida un segundo después es: {horadespues}")