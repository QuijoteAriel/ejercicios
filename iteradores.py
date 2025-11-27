from collections.abc import Iterable

# crear un iterador

my_list = [1, 2, 3, 4, 5, 6, 7]

# obtener el ietardor

my_iter = iter(my_list)

# usar el iterador

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# iterar cadenas

text = "hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)  # itera a travez de la cadena "hola mundo"

# iterar numeros
# limite
limit = 10

odd_iter = iter(range(1, limit, 2))
for n in odd_iter:
    print(n)


print("########################")


def contador_simple():
    print("Iniciando contador...")
    yield 1
    print("Continuando contador...")
    yield 2
    print("Terminando contador...")
    yield 3


# Llamar a la función generadora devuelve un objeto generador
generador = contador_simple()

# Iterar sobre el generador para obtener los valores
print("Primera llamada a next():")
print(next(generador))  # Salida: Iniciando contador..., 1

print("Segunda llamada a next():")
print(next(generador))  # Salida: Continuando contador..., 2

print("Tercera llamada a next():")
print(next(generador))  # Salida: Terminando contador..., 3

# Intentar obtener un cuarto valor resultará en un StopIteration
# print(next(generador)) # Esto lanzaría un StopIteration

print("\n--- Usando un bucle for (más común) ---")


def generar_numeros_con_yield():
    for i in range(5):
        yield i  # Cede un valor y pausa la ejecución


for numero in generar_numeros_con_yield():
    print(numero)
# Salida:
# 0
# 1
# 2
# 3
# 4


n = [2, 3, 4, 5, 6, 7, 8, 9]
scuare = [x**2 for x in n]
print(scuare)


# pares
par = [x for x in range(1, 21) if x % 2 != 0]
print(par)


lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  # True
print(isinstance(cadena, Iterable))  # True
print(isinstance(numero, Iterable))  # False
