m = int(input("Número de mes (1-12): "))

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("31 días")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("30 días")
elif m == 2:
    print("28 días")
else:
    print("Error")
