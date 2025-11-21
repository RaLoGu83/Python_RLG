altura = int(input("Introducir altura: "))
ast = "*"
espacios = " "
altura = altura - 1

print(espacios * altura + ast)

for i in range (1, altura):
    print(espacios * abs(i-altura) + ast + (espacios*((i-1)*2))+espacios + ast)
    
for j in range (altura, 0, -1):
    print(espacios * abs(j-altura) + ast + (espacios*((j-1)*2))+espacios + ast)
    
print(espacios * altura + ast)