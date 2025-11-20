contneg = 0
contpos = 0
num = 1

while num != 0:
    num = int(input("Introducir número diferente a 0: "))
    
    if num >= 0: #El 0 se cuenta como positivo al introducirlo como último número por la condición de este if
        contpos += 1
    else:
        contneg += 1
        
print(f"Hay {contpos} números positivos")
print(f"Hay {contneg} números negativos")