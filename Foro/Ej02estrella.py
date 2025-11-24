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

for i in range ( 3 ):
    print((espacios*i) + ast + (espacios*abs(3-i) + ast) + (espacios*abs(3-i)) + ast)
    
print(ast*altura)

for j in range ( 3, 0, -1 ):
    print((espacios*(j-1)) + ast + espacios +(espacios*abs(3-j) + ast) + espacios +(espacios*abs(3-j)) + ast)