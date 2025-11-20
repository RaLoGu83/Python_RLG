contneg = 0
contpos = 0
for i in range(100):
    num = int(input("Introducir número: "))
    
    if num >= 0:
        contpos += 1
    else:
        contneg += 1
        
print(f"Hay {contpos} números positivos")
print(f"Hay {contneg} números negativos")