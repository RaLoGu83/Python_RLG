A = int(input("Ingrese el lado A: "))
B = int(input("Ingrese el lado B: "))
C = int(input("Ingrese el lado C: "))

if (A**2 == B**2 + C**2) or (B**2 == A**2 + C**2) or (C**2 == A**2 + B**2):
    print("El triángulo es RECTÁNGULO")
elif A == B and B == C:
    print("El triángulo es EQUILÁTERO")
elif A == B or A == C or B == C:
    print("El triángulo es ISÓSCELES")
else:
    print("El triángulo es ESCALENO")
