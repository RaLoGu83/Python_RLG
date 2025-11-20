altura = int(input("Introduce la altura de la pirámide: "))
ast = "*"
espacios = " "

for i in range (1, altura):
    print(espacios*i + ((altura-i)*ast)+ast + ((altura-i)*ast))
    
print(altura* espacios + ast)