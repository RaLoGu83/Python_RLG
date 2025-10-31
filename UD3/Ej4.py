num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por cero"

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"El producto es: {producto}")
print(f"La división es: {division}")
