"""
## **Tuplas**

Las tuplas funcionan como listas, la única diferencia es que son inmutables,
es decir, una vez inicializadas, no podemos añadir, cambiar o borrar valores.

Para definir tuplas, utilizamos (). 
"""

# como no podemos agregar valores, no podemos inicializar tuplas vacías, 
# entonces siempre las inicializamos con algún valor:
compras = ("Manzana", "Sandía", "Plátano", "Galletas", "Leche", "Naranja", "Huevos")

# para accedar a un valor, hacemos igual que en las listas:
print(compras[2])

# si intentamos cambiar un valor por otro, nos sale un error
compras[2] = "Melocotón"

# el comando len() sigue funcionando
print("Longitud de la tupla: ", len(compras))

# pero el .append() no funciona
compras.append("Melocotón")