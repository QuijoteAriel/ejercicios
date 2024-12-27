import random

lista = [random.randint(1, 100) for _ in range(10)]
print("Lista:", lista)
print("Máximo:", max(lista))
print("Mínimo:", min(lista))
print("Media:", sum(lista) / len(lista))
