altura = int(input("Introducir altura: "))
ast = "*"
espacios = " "

for i in range (1, altura + 1):
    print(espacios*(altura-i) + (ast*i) + (ast*(i-1)) + espacios*(altura-i))
    
for j in range (1, altura + 1):
    print((espacios*j) + ast*(altura-1-j) +((ast)*(altura-j)))
