altura = int(input("Altura: "))
ast = "*"
espacios = " "

print(ast*altura)
for i in range (1, altura//2+1):
    print(ast + (espacios*i) + ast + espacios*(altura//2 - i)+ espacios + ast)

for j in range (altura//2-1, 0, -1):
    print(ast + (espacios*j) + ast + espacios*(altura//2 - j)+ espacios + ast)

print(ast*altura)
 