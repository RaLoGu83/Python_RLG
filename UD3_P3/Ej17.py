HH = int(input("Hora de salida (HH): "))
MM = int(input("Minutos de salida (MM): "))
SS = int(input("Segundos de salida (SS): "))

T = int(input("Tiempo de viaje en segundos: "))

salida_seg = HH * 3600 + MM * 60 + SS

llegada_seg = salida_seg + T

llegada_seg = llegada_seg % 86400 

HH_llegada = llegada_seg // 3600
MM_llegada = (llegada_seg % 3600) // 60
SS_llegada = llegada_seg % 60

print("Hora de llegada:", HH_llegada, ":", MM_llegada, ":", SS_llegada)
