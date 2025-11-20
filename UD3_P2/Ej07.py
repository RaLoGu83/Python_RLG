contneg = 0

for i in range(100):
    num = int(input("Introducir número: "))
    
    if num >= 0:
        continue
    else:
        contneg += 1
        
print(f"Hay {contneg} números negativos")