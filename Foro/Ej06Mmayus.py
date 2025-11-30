altura = int(input("Altura: "))
ast = "*"
espacios = " "

print(ast + (espacios*(altura-2)) + ast)

for i in range (1, altura//2):
    print(ast + (espacios*(i-1)) + ast + (espacios*(altura-2-2*i)) + ast +(espacios*(i-1)) + ast)

print(ast + (espacios*(altura//2-1)) + ast + (espacios*(altura//2-1)) + ast)

for j in range (0, altura//2):
    print(ast + (espacios*(altura-2)) + ast)