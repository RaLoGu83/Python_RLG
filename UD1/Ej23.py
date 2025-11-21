CPos = 0
CNeg = 0
Con = 0
N = 1

while N != 0 and Con < 5:
    N = int(input("Ingrese un número: "))
    Con = Con + 1
    
    if N%2 == 0:
        CPos = CPos + 1
    elif N==0:
        break
    else:
        CNeg = CNeg + 1
        
print(f"Números pares ingresados: {CPos}")
print(f"Números impares ingresados: {CNeg}")