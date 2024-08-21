'''
Actividad propuesta: 
Para finalizar de esta etapa, crearemos una función que generalice todo lo anterior de modo que siempre que sea necesario crear una caja,
podemos convocar esta funcion usando los parametros necesarios. Este será uno de los primeros usos avanzados de una función que
tendremos en Python.

La función debe recibir como parametros de entrada las dimensiones de la caja (longitud y número de líneas), el texto que debe
ser usado en el mensaje (Hola, Buenos dias, Buenas tardes, Buenas noches, ¿Qué tal?, etc..) y el nombre a ser puesto junto al texto.
Dados los inputs indicados, la función realizará la tarea de juntar el texto al nombre, crear y mostrar en pantalla la caja
en las dimensiones indicadas por medio de los parametros con el texto ya centralizado. Para hacerlo, podemos usar como base el código
que ya esta hecho en el archivo "2 - Caja con Saludo Tamaño Variable" que ya habéis hecho anteriormente.
'''

def crear_caja(MAX_HORIZONTAL, MAX_VERTICAL, texto, nombre):
    saludo = f"{texto}, {nombre}."
    tam = len(saludo)
    espacios = MAX_HORIZONTAL-tam
    mitad = espacios//2

    mensaje = (' '*mitad) + saludo + (' '*(mitad+espacios%2))

    linea_superior = " " + MAX_HORIZONTAL*"_"
    linea_inferior = "|" + MAX_HORIZONTAL*"_" + "|"
    linea_vacia = "|" + MAX_HORIZONTAL*" " + "|"

    for i in range(0,MAX_VERTICAL+1):
        if i == 0:
            print(f"{linea_superior}")

        elif i == MAX_VERTICAL//2 and MAX_VERTICAL%2==0:
            print(f"|{mensaje}|")

        elif i-1 == MAX_VERTICAL//2 and MAX_VERTICAL%2==1:
            print(f"|{mensaje}|")

        elif i == MAX_VERTICAL:
            print(f"{linea_inferior}")

        else:
            print(f"{linea_vacia}")

crear_caja(33, 7, 'Buenos días', 'Clóvis')
