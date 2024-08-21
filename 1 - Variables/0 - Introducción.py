# -*- coding: utf-8 -*-
"""
Al declarar variables, se recomienda el uso de palabras que de manera práctica 
indique que tipo de valor esta variable guardaría. Debemos tener en cuenta que 
hay ciertas restricciones al definir el nombre de las variables:

-> El nombre de una variable debe comenzar con una letra o un guion bajo (_).
-> No puede comenzar con un número ni contener caracteres especiales como !, @, $, etc.
"""

"""
**KEYWORDS**
Al nombrar variables, debemos tener en cuenta que ciertas palabras están reservadas 
en el lenguaje (palabras clave). Estas son utilizadas principalmente en comandos
específicos, por lo que es importante evitar su uso al declarar variables para 
garantizar la claridad y el funcionamiento adecuado del código.

Abajo está el listado de Keywords utilizadas en Python:


  False      await      else       import     pass
  None       break      except     in         raise
  True       class      finally    is         return
  and        continue   for        lambda     try
  as         def        from       nonlocal   while
  assert     del        global     not        with
  async      elif       if         or         yield
"""

"""
### **Caracteres permitidos:**

-> Después del primer caracter, puedes usar letras, números 
y guiones bajos en el nombre de una variable.

-> Es importante fijar que Python hace la diferenciación entre mayúsculas y minúsculas, es decir, 
una variable llamada `Nombre` y otra llamada `nombre` son consideradas como dos cosas diferentes en Python.

Al seguir las restricciones mencionadas anteriormente, tenemos la libertad de elegir 
nombres para nuestras variables según lo que sea más conveniente para nuestro código.
"""


### Creación e inicialización de variables por defecto
nombre = 'Clóvis Magno'  # tipo string (str)
edad = 26   # tipo entero (int)
altura = 1.80   # tipo real (float), son números con parte decimal
humano = True   # tipo booleano (bool), puede valer True o False
peliculas_favoritas = ["Spiderman", "Terminator", "Interestellar"] # tipo lista
notas = {"Matemáticas": 8, "Biología": 7, "Latín": 5, "Ciencias": 7, "Francés": 4.99} # tipo diccionario



### Imprimiendo los valores de las variables por pantalla
print("Te llamas:", nombre)
print(f"Tienes {edad} años.")
print(f"Mides {altura} metros de altura.")
print("Tus peliculas favoritas son: ", peliculas_favoritas)
print("Estas son tus notas: ", notas)


### Tipos
# Para comprobar los tipos de variables podemos usar el comando type tal como se muestra abajo.
print("Tipos:")
print("El tipo de la variable 'nombre' es: ", type(nombre))
print("El tipo de la variable 'edad' es: ", type(edad))
print("El tipo de la variable 'altura' es: ", type(altura))
print("El tipo de la variable 'humano' es: ", type(humano))
print("El tipo de la variable 'peliculas_favoritas' es: ", type(peliculas_favoritas))
print("El tipo de la variable 'notas' es: ", type(notas))


### Creación e inicialización de variables por teclado
# Al inicializar las variables por teclado es necesario indicar el tipo de la variable si esta NO es de tipo string (str)
nombre = input("¿Cómo te llamas? ")  # como nombre es de tipo str, no es necesario indicarlo
edad = int(input("¿Cuántos años tienes? ")) # la edad es un número entero, por eso se pone int
altura = float(input("¿Cuánto mides? "))  # ya la altura es un número con parte decimal, por eso se pone float

print("Te llamas:", nombre)
print(f"Tienes {edad} años.") # esta es otra manera de imprimir el valor de una variable por teclado
print(f"Mides {altura} metros de altura.")


### Operando con variables numéricas
"""
Estos son los operadores básicos que podemos utilizar con las variables numéricas
Sumas: +
Restar: -
División: /
División entera: // 
Multiplicación: *
Resto: %
"""
edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")
edad = edad + 1
print(f"Ahora tienes {edad} años.")
anyo_actual = 2024
anyo_nacimiento = anyo_actual - edad
print(f"Has nacido en {anyo_nacimiento}")

print("El resto de dividir 15 entre 4 es: ", 15 % 4)

print("El resultado de la división de 15 entre 4 es: ", 15 / 4)

print("El resultado de la división entera de 15 entre 4 es: ", 15 // 4)

print("15 multiplicado por 4 es: ", 15 * 4)

