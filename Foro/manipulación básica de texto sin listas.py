# Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.

# cadena = str(input("Introduce una cadena de texto: "))

# for i in range(len(cadena)):
#     print(cadena[i])


# Concatenar caracteres o cadenas utilizando el operador + para formar nuevas cadenas.

# cadena = str(input("Introduce una cadena de texto: "))
# cadena2 = str(input("Introduce otra cadena de texto: "))

# print(cadena + " " + cadena2)


# Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

# cadena = str(input("Mete la cadena: ")) 
# contador = 0
# for i in range(len(cadena)):
#     contador += 1
# print(contador)


# Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).
# Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.

# cadena=input("escribe texto: ")
# contador=0
# for i in range(len(cadena)):
#     if(cadena[i]=="a"):
#         contador+=1
#     else:
#         contador+=0
# if (contador>1):
#     print("existe ese caracter")
# else:
#     print("no existe ese caracter")


# Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).

# cadena=input("escribe texto: ")
# cacho=cadena[1:4]
# print(cacho)


# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).

# texto = input("Escribe un texto: ")
# resultado = ""

# for c in texto:
#     codigo = ord(c)  

#     if 97 <= codigo <= 122:
#         resultado += chr(codigo - 32)
#     else:
#         resultado += c 

# print("MAYÚSCULAS:", resultado)


# Leer una cadena y contar cuántas vocales contiene.

# palabras=input("escribe palabras:")
# cont=0
# for i in range(len(palabras)):
#     if(palabras[i] in "aeiou"):
#         cont+=1
#     else:
#         cont+=0
# print(cont)


# Leer una cadena y contar cuántos caracteres son letras mayúsculas.

# cadena=input("escribe letras: ")
# cont=0
# for i in range(len(cadena)):
#     if(cadena[i].isupper()):
#         cont+=1
# print(cont)

# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

# text = input("Escribe un texto: ")
# nuevo = ""

# vocales = "aeiouAEIOU"

# for c in text:
#     if c in vocales:
#         nuevo += c + c  
#     else:
#         nuevo += c     

# print("Nueva cadena:", nuevo)

# Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.
# cadena = input("Escribe un cadena: ")
# invertida = ""

# for c in cadena:
#     invertida = c + invertida  

# print("Invertida:", invertida)

# Leer una cadena y eliminar todos los espacios, construyendo una cadena continua
# cadena = input("Escribe un cadena: ")
# sin_espacios = ""

# for c in cadena:
#     if c != " ":          
#         sin_espacios += c

# print("Cadena sin espacios:", sin_espacios)

# Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene
# cadena = input("Escribe un cadena: ")
# contador = 0

# for c in cadena:
#     if "0" <= c <= "9":   
#         contador += 1

# print("Cantidad de números:", contador)

# Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'
# cadena = input("Escribe un cadena: ")
# nuevo = ""

# vocales = "aeiouAEIOU"

# for c in cadena:
#     if c in vocales:
#         nuevo += "*"
#     else:
#         nuevo += c

# print("Nueva cadena:", nuevo)

# Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).
# cadena1 = input("Escribe la primera cadena: ")
# cadena2 = input("Escribe la segunda cadena: ")

# resultado = ""

# for c in cadena1:
#     resultado = resultado + c

# for c in cadena2:
#     resultado = resultado + c

# print("Resultado:", resultado)

# Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.
# cadena = input("Escribe una cadena: ")

# nueva = ""

# for c in cadena:
#     contador = 0
#     for x in cadena:
#         if x == c:
#             contador += 1

#     if contador > 1 and c not in nueva:
#         nueva += c

# print("Caracteres repetidos:", nueva)

# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).
# cadena = input("Escribe una cadena: ")
# consonantes = ""

# vocales = "aeiouAEIOU"

# for c in cadena:
#     if ("a" <= c <= "z" or "A" <= c <= "Z") and c not in vocales:
#         consonantes += c

# print("Consonantes:", consonantes)
