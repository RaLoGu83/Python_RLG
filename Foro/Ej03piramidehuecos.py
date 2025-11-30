altura = int(input("Altura: "))
ast = "*"
espacios = " "

print(altura*espacios + ast)
for i in range (1, altura):
    
    if i>2 and i%2 != 0 and i != altura-1:
        print(espacios*(altura-i)+(ast+espacios)*(i + 1))
    elif i == altura-1:
        print(espacios+ast*((altura*2)-1))
    else:
        print((espacios*(altura-i)+ast+espacios*((i*2)-1)+ast))
