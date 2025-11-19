altura = int(input("Introduce la altura: "))
ast = "4"
espacios = " "
print(ast)

for i in range (altura-2):
    print( (ast) + (espacios * i) + (ast) )
    print(end="")   


print(ast * altura)
    

