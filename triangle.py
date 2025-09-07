''' def print_triangle(size, character):
    """
    Crea una cadena de texto que representa un triángulo.

    Args:
        size (int): El número de filas del triángulo.
        character (str): El carácter con el que se construye el triángulo.

    Returns:
        str: La cadena de texto del triángulo.
    """
    # Inicializa una cadena vacía para construir el triángulo
    triangle_string = ""

    # Itera sobre cada fila del triángulo, desde la fila 0 hasta la 'size - 1'
    for row in range(size):
        # Calcula el número de espacios necesarios para centrar el triángulo
        num_spaces = size - row - 1

        # Calcula el número de caracteres necesarios para la fila actual
        num_characters = 2 * row + 1

        # Construye la fila: agrega los espacios y luego los caracteres
        line = " " * num_spaces + character * num_characters

        # Agrega la fila a la cadena del triángulo
        triangle_string += line

        # Si no es la última fila, agrega un salto de línea
        if row != size - 1:
            triangle_string += "\n"

    # Retorna la cadena completa del triángulo
    return triangle_string

print(print_triangle(3,"#"))

''' 

def hacer_triangulo(filas, simbolo):
    # La variable "dibujo" va a guardar el triángulo que hagamos
    dibujo = ""

    # Vamos a repetir esto para cada fila del triángulo
    for numero_de_fila in range(filas):
        # Esta variable es para los espacios, ¡son los que centran el triángulo!
        espacios = " " * (filas - numero_de_fila - 1)

        # Esta es la parte de los símbolos, para que sean más en cada fila
        simbolos = simbolo * (2 * numero_de_fila + 1)

        # Ahora juntamos los espacios con los símbolos para hacer la fila completa
        fila_terminada = espacios + simbolos

        # Y agregamos la fila completa a nuestro "dibujo"
        dibujo = dibujo + fila_terminada

        # Si la fila no es la última, ponemos un salto de línea
        if numero_de_fila < filas - 1:
            dibujo = dibujo + "\n"

    # Al final, le decimos a la función que nos dé el "dibujo"
    return dibujo

print(hacer_triangulo(4,'$'))
