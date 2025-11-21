CPos = 0
CNeg = 0

for i in range(100):
    N = int(input("Ingrese un número: "))
    
    if N%2 == 0:
        CPos = CPos + 1
    else:
        CNeg = CNeg + 1
        
print(f"Números pares ingresados: {CPos}")
print(f"Números impares ingresados: {CNeg}")