# *   *   *
#  *  *  *
#   * * *
# *********
#   * * *
#  *  *  *
# *   *   *

altura = int(input("Introduce la altura: "))
ast = "*"
espacios = " "

for i in range (1, altura//2 ):
    print((espacios*(i-1)) + ast + (espacios*abs(altura//2-i) + ast) + (espacios*abs(altura//2-i)) + ast)
    
print(ast*altura)

for j in range ( altura//2, 1, -1 ):
    print((espacios*((j-1)-1)) + ast + espacios +(espacios*abs(altura//2-j) + ast) + espacios +(espacios*abs(altura//2-j)) + ast)