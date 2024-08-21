"""
## **Diccionarios**

Este tipo de variable es la que más se diferencia de las otra dos mencionadas 
anteriormente. Aquí también podemos guardar vários valores, la diferencia que ahora 
estos valores no estarán marcados por su posición dentro de la variable, 
los identificaremos por la **clave** que lo acompaña.

En Python, un diccionario es un tipo de variable que permite almacenar pares clave-valor.
Cada elemento en un diccionario consiste en una clave (única) y su respectivo valor 
asociado. Veamos como crealos y utilizarlos.
"""

# podemos crear diccionarios vacíos utilizando una de las formas abajo y después agregar sus valores
notas = {}
notas = dict()

# pero podemos también crear diccionarios ya inicializado con sus claves y sus valores
notas = {"Matemáticas": 8, "Biología": 7, "Latín": 5, "Ciencias": 7, "Francés": 4.99}
print(notas)

"""
Diferente de las listas, para usar un diccionario ya no indicamos el valor que 
buscamos por la posición que este ocupa dentro de la variable, 
sino por la clave que está asociada a este valor determinado. 
Por ejemplo, si quiero saber la nota asociada a la asignatura "Biología", 
basta con indicar la clave:
"""

print("La nota en la asignatura Biología es: ", notas["Biología"])

# Lo mismo para matemáticas
print("La nota en la asignatura Matemáticas es: ", notas["Matemáticas"])

"""
Si queremos añadir un valor más al diccionario, es muy sencillo, veamos:
"""

# agregando la nota de Programación
print("Antes de agregar la nota de Programación: ", notas)
notas["Programación"] = 8.5
print("Después de agregar la nota de Programación: ", notas)

# Podemos también obtener cuales claves existen en el diccionario usando el comando .keys()
claves = notas.keys()
print(claves)

# También podemos obtener todos los valores usando el comando .values()
valores = notas.values()
print(valores)

# Podemos cambiar el valor de una clave de la siguiente manera:
print(notas)
notas["Programación"] = 10
print(notas)
