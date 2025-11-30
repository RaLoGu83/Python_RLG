altura = int(input("Altura (solo números impares): "))
ast = "*"
espacios = " "

print(ast*altura)

for i in range (2, altura//2):
    print(ast + (espacios*(i-1)) + ast + (espacios*(altura-2-2*i)) + ast +(espacios*(i-1)) + ast)


print(ast + (espacios*(altura//2-1)) + ast + (espacios*(altura//2-1)) + ast)
print(ast + (espacios*(altura-2)) + ast)
print(ast + (espacios*(altura//2-1)) + ast + (espacios*(altura//2-1)) + ast)

for j in range (altura//2 -1, 1, -1):
    print(ast + (espacios*(j-1)) + ast + (espacios*(altura-2-2*j)) + ast +(espacios*(j-1)) + ast)

print(ast*altura)
