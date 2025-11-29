d = int(input("Distancia entre los vehículos (km): "))
v1 = int(input("Velocidad del vehículo que va adelante (km/h): "))
v2 = int(input("Velocidad del vehículo que va detrás (km/h): "))

vel_rel = v2 - v1

if vel_rel <= 0:
    print("El vehículo de atrás no alcanzará al de adelante.")
else:
    tiempo_horas = d / vel_rel

    tiempo_minutos = tiempo_horas * 60

    print("El vehículo más rápido alcanzará al otro en", tiempo_minutos, "minutos.")
