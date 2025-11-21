altura = int(input("Introduce la altura: "))

ast = "*"
espacios = " "

for i in range (1, altura + 1):
    print((ast*2*altura)+ast)
    print((ast + espacios)*altura + ast)