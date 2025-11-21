num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} {num2}")
elif num2 > num1:
    print(f"{num2} {num1}")
else:
    print("Los números son iguales")