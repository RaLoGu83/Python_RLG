altura = int(input("Introduce la altura: "))
ast = "*"
espacios = " "

print((altura * espacios)+ espacios + ast)

for i in range (1, altura):
    print( espacios*(altura - i) + ast + espacios * (i) + ast )
    print(end="")  
    
for j in range (altura, 0, -1):
    print( espacios*(altura - j) + ast + espacios * (j) + ast )
    print(end="")  

print((altura*espacios) + espacios + ast)