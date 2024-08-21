
"""
## **Listas**
Las listas son una de las variables contenedoras más populares en Python, 
se destaca por su versatilidad para uso en las más diferentes situaciones. Veámos como usarlas.
"""

# Podemos crear listas vacías siguiendo una de las maneras abajo:
lista_1 = []
print("Lista 1: ", lista_1)

lista_2 = list()
print("Lista 2: ", lista_2)

# También podemos crear listas ya inicializadas con algunos valores
compras = ["Manzana", "Sandía", "Plátano", "Galletas", "Leche", "Naranja", "Huevos"]

print("Lista de compras: ", compras)


"""
La ventaja de trabajar con listas es que podemos acceder a cada uno de sus 
valores de manera independiente y operar como más nos convenga. Miremos cómo hacerlo:
"""
# Así accedemos a los valores de manera individual: 
print(compras[0])
print(compras[1])
print(compras[2])

"""
Como podemos observar arriba, para utilizar los valores contenidos en una lista de manera individual, 
solo necesitamos indicar ese valor por su posición en la lista (su ÍNDICE o INDEX). 
Los índices SIEMPRE comienzan desde cero, lo que significa que el primer elemento 
en una lista se encuentra en la posición 0, el segundo en la posición 1, y así sucesivamente.

A una lista podemos hacer también una serie de operaciones, como añadir elementos, borrar elementos, 
cambiar el valor de algún elemento, saber su tamaño, ¡entre muchas otras más!
"""

# Agregando elementos: comando .append(elemento)
compras = ["Manzana", "Sandía", "Plátano", "Galletas", "Leche", "Naranja", "Huevos"]
print("Compras: ", compras)

nuevo_producto = input("¿Qué deseas añadir a la lista de compras? ")      # guardamos el nuevo producto en la variable 'nuevo_producto'
compras.append(nuevo_producto)    # agregamos ese iten dentro de la lista
print(compras)      # enseñamos la lista actualizada

# Borrando elementos por su valor: comando .remove(elemento)
compras.remove("Manzana")
print(compras)

# Borrando elementos por su posición: comando .pop(posicion_del_elemento)
compras.pop(2)
print(compras)

# Obteniendo la longitud de una lista: comando len(lista)
longitud = len(compras)
print(f"La lista tiene {longitud} elementos")

# Cambiando el valor de algún elemento en la lista:
print("Lista antes del cambio: ", compras)
compras[0] = "Melocotón"
print("Lista después del cambio: ", compras)