'''
Explicación con más detalles sobre las funciones 
disponible en https://drive.google.com/file/d/1F7GS8-1LEKGD1-IJF-oNTsMVCaGzpf4y/view?usp=sharing
'''

num_1 = 2
num_2 = 3
suma = num_1 + num_2
print("La suma es", suma)



#############################
# fución sin parámetros y sin return
def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2
    print("La suma es", suma)

sumador()
###################################
# fución con parámetros y sin return

def sumador(num_1, num_2):
    suma = num_1 + num_2
    print("La suma es", suma)

num_1 = 2
num_2 = 3
sumador(num_1,num_2)



#############################
# fución sin parámetros y sin return
def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2

suma = 0
sumador()
print(suma)
##############################
# fución sin parámetros y con return
def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2
    return suma

suma = 0
suma = sumador()
print(suma)
##############################

# fución con parámetros y con return
def sumador(num_1, num_2):
    suma = num_1 + num_2
    return suma

num_1 = 2
num_2 = 3
suma = 0
suma = sumador(num_1, num_2)
print("La suma es", suma)



################################

num_1 = 10
num_2 = 5

suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)
##################################

def calculadora():
    num_1 = 10
    num_2 = 5

    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 / num_2

    print("La suma es: ", suma)
    print("La resta es: ", resta)
    print("La multiplicación es: ", multiplicacion)
    print("La división es: ", division)

##################################

# Actividad propuesta: hacer una función calculadora que reciba 2 valores como parámetros y 
# devuelva el valor de la suma, resta, multiplicación y división de esos dos valores
def calculadora(num_1, num_2):
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 / num_2
    return suma, resta, multiplicacion, division

suma = 0
resta = 0
multiplicacion = 0
division = 0

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
suma, resta, multiplicacion, division = calculadora(n1, n2)

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)

