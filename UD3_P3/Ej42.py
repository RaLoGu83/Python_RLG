cadena = str(input("Introduce texto acaba en espacio: "))

for i in range (len(cadena)):
    
    if cadena[i] in "aeiou":
        print("VOCAL")
    elif cadena[i] == " ":
        break
    else:
        print("NO VOCAL")