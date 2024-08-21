# Escribe tu código aquí :-)

numero = 0
while numero <= 10:
    print(numero)
    numero = numero+1

# actividad propuesta: pedir un número al usuario y repetir código mientras dicho número sea mayor que 100

numero = int(input("¿Cuál número eliges? "))
while numero > 100:
    print("Número inválido, el número necesita ser menor que 100.")
    numero = int(input("¿Cuál número eliges? "))

print("EL número elegido es: ", numero)