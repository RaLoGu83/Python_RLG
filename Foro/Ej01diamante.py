altura = int(input("Introducir altura: "))
ast = "*"
espacios = " "
# Este código printea 1 linea extra en el primer bucle y 2 extra en el segundo bucle
print(espacios * altura + ast)

for i in range (1, altura + 1):
    print(espacios * abs(i-altura) + ast + (espacios*((i-1)*2))+espacios + ast)
    
for j in range (altura, 0, -1):
    print(espacios * abs(j-altura) + ast + (espacios*((j-1)*2))+espacios + ast)
    
print(espacios * altura + ast)