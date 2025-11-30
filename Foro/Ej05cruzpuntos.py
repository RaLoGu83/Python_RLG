altura = int(input("Altura: "))
ast = "*"
espacios = " "
puntos = "."

print((puntos + espacios)*altura)

for i in range (1, altura//2):
    print((puntos+espacios)*(i)+(ast+espacios)+(puntos+espacios+ast+espacios)*(altura//2-i)+(puntos+espacios)*(i))

print((ast+espacios)*altura)

for j in range (altura//2 - 1, 0, -1):
    print((puntos+espacios)*(j)+(ast+espacios)+(puntos+espacios+ast+espacios)*(altura//2-j)+(puntos+espacios)*(j))

print((puntos + espacios)*altura)
