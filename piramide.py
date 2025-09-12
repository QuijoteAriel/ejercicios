def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return triangle


print(print_triangle(4, '&'))

def print_inverted_triangle(size, character):
    """
    Imprime un triángulo invertido de un tamaño y carácter dados.
    """
    inverted_triangle = ''
    # El bucle va desde el tamaño máximo hasta 1
    for i in range(size, 0, -1):
        # Calcula los espacios. Los espacios aumentan con cada línea
        spaces = " " * (size - i)
        # Calcula los caracteres. Los caracteres disminuyen con cada línea
        # La fórmula es (2 * i - 1) para mantener la forma de triángulo
        characters_to_print = character * (2 * i - 1)
        inverted_triangle += spaces + characters_to_print
        if i > 1:
            inverted_triangle += "\n"
    return inverted_triangle

print(print_inverted_triangle(4, '&'))

p= input('dime un numero o palabras ')

if p[::-1] == p:
    print('es palindromo')
else:
    print('no es palindromo')
