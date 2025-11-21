N1 = int(input("Introduce el primer número: "))
N2 = int(input("Introduce el segundo número: "))
N3 = int(input("Introduce el tercer número: "))

if N1 > N2 and N1 > N3:
    print(f"El número mayor es: {N1}")
elif N2 > N1 and N2 > N3:
    print(f"El número mayor es: {N2}")
elif N3 > N1 and N3 > N2:
    print(f"El número mayor es: {N3}")
elif N1 == N2 and N1 > N3:
    print(f"Los números mayores son: {N1} y {N2}")
elif N1 == N3 and N1 > N2:
    print(f"Los números mayores son: {N1} y {N3}")
elif N2 == N3 and N2 > N1:
    print(f"Los números mayores son: {N2} y {N3}")
else:
    print("Los tres números son iguales.")
    