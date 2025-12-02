n1 = int(input("Ingrese el número de primos: "))
num = 2
cont = 0

while cont < n1:
    es_primo = True
    i = 2
    
    while i * i <= num:
        if num % i == 0:
            es_primo = False
            break
        i += 1

    if es_primo:
        print(num, end=" ")
        cont += 1

    num += 1
