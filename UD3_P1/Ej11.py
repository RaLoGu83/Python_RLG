num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")