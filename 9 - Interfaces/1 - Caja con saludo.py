'''
Empezaremos a trabajar ahora con las interfaces de interacción en Python. Primero
haremos interfaces manualmente usando simbolos del teclado. El primer proyecyo es
el siguiente: Crear una caja de texto donde se muestre un saludo (Hola, buenos días, buenas tardes, etc)
junto al nombre del usuario que será introducido por teclado.

La mensaje final tiene que estar centralizada en la caja tanto verticalmente como horizontalmente y la caja
debe adaptarse a diferentes nombres y mantener su forma independiente de cuantos caracteres tenga el nombre
desde que el nombre junto al saludo no resulte en un texto mayor que la longitud horizontal de la caja.

Ejemplos de outputs validos:

1)
 ______________________________
|                              |
|                              |
|     Hola, Clóvis Magno.      |
|                              |
|______________________________|


2)
 ______________________________
|                              |
|                              |
|        Hola, Clóvis.         |
|                              |
|______________________________|


3)
 ______________________________
|                              |
|                              |
|  Buenos días, Clóvis Magno.  |
|                              |
|______________________________|

'''

MAX = 25 # máximo de espacios en la horizontal
nombre = input("¿Cuál es tu nombre? ")
saludo = f"Hola, {nombre}."
tam_texto = len(saludo)
espacios_total = MAX - tam_texto # total de espacios en vacios
espacios_mitad = espacios_total//2 # division para saber cuantos espacios son necesarios de cada lado

texto_espacio_izq = " "*espacios_mitad # espacios a la izquierda
texto_espacio_der = " "*espacios_mitad # espacios a la derecha

# el if abajo sirve para ajustar la caja si el número total de espacios que debe ser repartido para cada lado
# es un numero par (error que ocurre por la división exacta por 2 en 'espacios_total//2').
# Cuando es así, tenemos que restar un espacio a la izquierda o a la derecha pra que la caja mantenga su forma
# (en nuestro caso, vamos restar a la izquierda)

if espacios_total%2 == 0:
    texto_espacio_der = " "*(espacios_mitad-1)

# printamos la caja
print(" ________________________")
print("|                        |")
print("|                        |")
print(f"|{texto_espacio_izq}{saludo}{texto_espacio_der}|")
print("|                        |")
print("|________________________|")
