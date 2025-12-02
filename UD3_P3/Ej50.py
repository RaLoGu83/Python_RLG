km1 = 70
km2 = 150
vel = float(input("Velocidad de los coches (km/h): "))

distancia = km2 - km1
tiempo = distancia / (2 * vel)
encuentro = km1 + vel * tiempo

print("Se encontrarán en el km:", encuentro)
