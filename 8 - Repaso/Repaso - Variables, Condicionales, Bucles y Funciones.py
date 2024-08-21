# 1 - Variables

# Crear y definir variables
nombre = "Clóvis Magno"
edad = 25
altura = 1.80
print("El nombre es: ", nombre)
print("La edad es: ", edad)

# Entradas por teclado
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
altura = float(input("¿Cuál es tu altura? "))

print("El nombre es: ", nombre)
print("La edad es: ", edad)

# Enseñando valores en pantalla
nombre = "Clóvis Magno"
apellido = "Santos"
print("El nombre es " + nombre + " y el segundo apellido es " + apellido + ".")
print("El nombre es", nombre,"y el segundo apellido es", apellido,".")

edad = 25

# print(nombre + "tiene" + edad + "años.")
print(nombre,"tiene", edad,"años.")
print(f"{nombre} tiene {edad} años!")
print("{} TIENE {} AÑOS.".format(nombre, edad))

#################################################################################
# 2 - Condicionales

temperatura = int(input("¿Cuál la temperatura del paciente? "))

if temperatura > 37:
    print("El paciente tiene fiebre.")
else:
    print("El paciente no tiene fiebre.")

'''
SÓLIDO: MENOS QUE 0ºC
LÍQUIDO: 0ºC HASTA 100ºC
GASEOSO: MÁS QUE 100ºC
'''

temperatura_agua = float(input("¿Cuál es la temperatura medida del água? "))

if temperatura_agua < 0:
    print("El agua está en estado sólido.")
elif temperatura_agua >= 0 and temperatura_agua < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.")

'''
Otra manera de hacer lo mismo seria usando dos elif
Es importante recordar que los elif y los else solo se ejecutan si todas las
condiciones anteriores a éstos son falsas. Si hay una que sea verdadera, todos los elif
y los else que estén por debajo serán ignorados en la ejecución. Así, usar elif y else es
una manera de asegurarnos que solo una opción se ejecutará cuando así se desea o sea necesário.

En la opción abajo, por ejemplo, no hace falta usar un condicional compuesto como antes en la
segunda condición, ya que si temperatura_agua > 100, el if se ejecuta, y todo lo de abajo
será ignorado. Entonces, aunque una temperatura mayor que 100 sea también mayor que 0, usando los
elif ahorramos el uso de condicionales como 'temperatura_agua > 0 and temperatura_agua < 100', ya que si 
el programa llega en este bloque esto indicaría que el primer if es falso, por lo cual, la temperatura
ya es menor que 100. 
'''


if temperatura_agua > 100:
    print("El água está en estado gaseoso.")
if temperatura_agua > 0:
     print("El água está en estado líquido.")
if temperatura_agua < 0:
   print("El água está en estado sólido.")

#################################################################################
# 3 - Bucles

# escribir los números del 0 al 10 (el ultimo valor no está incluido)
for numero in range(0,10):
    print(numero)

# escribir los números del 0 al 10 (el ultimo valor no está incluido)

numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1

###################################
pares = []
for numero in range(0,10):
    if numero%2 == 0:
        pares.append(numero)
print(pares)

numero = 0
pares = []
while numero < 10:
    if numero%2 == 0:
        pares.append(numero)
    numero = numero + 1
print(pares)

#################################################################################
# 4 - Funciones

# FUNCIÓN SIN PARAMETROS O RETURN
def contar_letras():
    nombre = input("¿Cuál es tu nombre? ")
    letras = len(nombre) # el comando len indica el tamaño de una lista o de una string
    print(f"Tu nombre tiene {letras} letras.")

contar_letras()

# FUNCIÓN CON PARAMETRO
def contar_letras(nombre):
    letras = len(nombre)
    print(f"Tu nombre tiene {letras} letras.")

nombre = input("¿Cuál es tu nombre? ")
contar_letras(nombre)

# FUNCIÓN CON PARAMETRO Y RETURN
def contar_letras(nombre):
    letras = len(nombre)
    return letras

nombre = input("¿Cuál es tu nombre? ")
letras = contar_letras(nombre)
print(f"Tu nombre tiene {letras} letras.")

def vocales_y_consonantes(nombre):
    lista_vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    vocales = 0
    consonantes = 0
    for letra in nombre:
        if letra in lista_vocales:
            vocales = vocales + 1
        else:
            consonantes = consonantes + 1

    return vocales, consonantes

nombre = "Clóvis"
vocales, consonantes = vocales_y_consonantes(nombre)
print(f"El nombre {nombre} tiene {vocales} vocales y {consonantes} consonantes.")