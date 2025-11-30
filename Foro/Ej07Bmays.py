altura = int(input("Altura: "))
ast = "*"
espacios = " "

print(altura*ast)
for i in range (0, altura-2):
    if i%2 == 0:
        print((ast+espacios)*(altura//2) + ast)
    else:
        print(ast + (espacios*(altura-1))+ast)
print(altura*ast)
