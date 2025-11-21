N1 = int(input("Introduce el primer número: "))
N2 = int(input("Introduce el segundo número: "))

if N1 > N2:
    print(f"El número mayor es: {N1}")
elif N2 > N1:
    print(f"El número mayor es: {N2}")
else: 
    print("Ambos números son iguales.")