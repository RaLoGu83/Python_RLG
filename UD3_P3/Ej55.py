while True:
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Has seleccionado Opción 1")
    elif opcion == "2":
        print("Has seleccionado Opción 2")
    elif opcion == "3":
        print("Has seleccionado Opción 3")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")
