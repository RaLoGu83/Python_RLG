print("Bienvenido a su Cajero Virtual")
dinero = 1000

while True:
    n = int(input("Introduce 1. Ingresar dinero en cuenta 2. Retirar dinero de la cuenta 3. Salir"))
    
    if n == 1:
        dinero = dinero + int(input("¿Cuánto dinero desea ingresar? "))
        print(f"Su saldo actual es de {dinero} $")
    elif n == 2:
        cantidad = int(input("¿Cuánto dinero desea retirar? "))
        if cantidad > dinero:
            print("No dispone de saldo suficiente")
        else:
            dinero = dinero - cantidad
            print(f"Su saldo actual es de {dinero} $")
    elif n == 3:
        print("Saliendo del programa...")
        break