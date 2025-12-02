altura = int(input("Altura: "))
ast = "*"
espacios = " "

for i in range(altura):
    if i == altura-1:
        print(espacios*altura+(ast+espacios)*(altura))
    elif i == 0:
        print(espacios*altura+espacios*(altura-1) + ast )
    else:
        print(espacios*altura+(espacios*(altura-i-1)+ast+espacios*(i*2-1)+ast))


for i in range (altura):
    if i == altura-1:
        print((ast+espacios)*(altura) + (ast+espacios)*(altura))
    elif i == 0:
        print(espacios*(altura-1) + ast + (espacios*(altura*2-1)) + ast)
    else:
        print((espacios*(altura-i-1)+ast+espacios*(i*2-1)+ast) + (espacios*(altura-i-1)) + (espacios*(altura-i)+ast+espacios*(i*2-1)+ast))
    
        
