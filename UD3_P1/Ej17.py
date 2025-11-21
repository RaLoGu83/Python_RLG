usuario = str(input("Introduce tu nombre de usuario: "))
password = str(input("Introduce tu contraseña: "))

if usuario == "admin" and password == "1234":
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario incorrecto")