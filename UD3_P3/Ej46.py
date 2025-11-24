base = int(input("Base: "))
expo = int(input("Exponente: "))
resultado = 1

for i in range(expo):
    resultado = resultado * base
    
print(resultado)