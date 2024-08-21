# Escribe tu código aquí :-)

'''
for numero in range(0,10): # repite mientras numero < 10 ( 10 no incluido)
    print(numero)
'''

compras = ["Manzana", "Sandía", "Plátano", "Galleta", "Pasta", "Naranja", "Huevos"]


print(compras[0])
print(compras[1])
print(compras[2])
print(compras[3])
print(compras[4])


for i in range(0,10):
    print(i)

print("La variable i vale", i)


# activiadad propuesta: imprimir los elementos de una lista de manera individual utilizando bucle for
print("Primera manera: ")
for i in range(0, 7):
    print(compras[i])

# manera recomendable utilizando len para el limite:
print("\nSegunda manera: ")
for i in range(0, len(compras)):
    print(compras[i])


# otra manera útil para usar con listas:
print("\nTercera manera: ")
for elemento in compras:
    print(elemento)
